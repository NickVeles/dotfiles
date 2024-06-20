const hyprland = await Service.import("hyprland")
const notifications = await Service.import("notifications")
const network = await Service.import("network")
const bluetooth = await Service.import("bluetooth")
const mpris = await Service.import("mpris")
const audio = await Service.import("audio")
const battery = await Service.import("battery")
const systemtray = await Service.import("systemtray")

// TODO: Network() wifi hasn't been tested
// TODO: Battery() hasn't been tested
// TODO: Pomodoro() primary click doesn't work


// Variables
const calendarVisible = Variable(false)


// Workspaces Widget
function Workspaces() {

    const activeId = hyprland.active.workspace.bind("id")

    const workspaces = hyprland.bind("workspaces")
        .as(ws => ws
            .filter(({ id }) => id > 0) // Filter out special workspaces
            .sort((a, b) => a.id - b.id) // Sort workspaces
            .map(({ id }) => Widget.Button({
                // cursor: "pointer".
                on_clicked: () => hyprland.messageAsync(`dispatch workspace ${id}`),
                child: Widget.Label(`${id}`),
                class_name: activeId.as(i => `${i === id ? "focused" : ""}`),
            }))
        )

    return Widget.Box({
        class_name: "workspaces",
        children: workspaces,
    })
}


// Notifications Widget
function Notifications() {

    const popups = notifications.bind("popups")

    return Widget.Box({
        spacing: 4,
        class_name: "notifications",
        visible: popups.as(p => p.length > 0),
        children: [
            Widget.Icon({
                icon: "preferences-system-notifications-symbolic",
            }),
            Widget.Label({
                label: popups.as(p => p[0]?.summary || ""),
            }),
        ],
    })
}


// SysTray Widget
function SysTray() {
    const items = systemtray.bind("items")
        .as(items => items.map(item => Widget.Button({
            child: Widget.Icon({ icon: item.bind("icon") }),
            on_primary_click: (_, event) => item.activate(event),
            on_secondary_click: (_, event) => item.openMenu(event),
            tooltip_markup: item.bind("tooltip_markup"),
        })))

    return Widget.Box({
        class_name: "systray",
        children: items,
    })
}


// Pomodoro Widget
function Pomodoro() {

    // Initial Seconds
    const initSec = Variable(45 * 60)

    const runTime = Variable(initSec, {
        poll: [1000, () => initSec.value--]
    })

    function getTooltip() {
        const minutes = Math.floor(runTime.value / 60)
        const seconds = runTime.value % 60

        return `${minutes}m ${seconds}s`
    }

    function getIcon() {
        const icon = Math.round((runTime.value / 2700) * 61)

        return `pomodoro-indicator-light-${icon}`
    }

    return Widget.Button({
        class_name: "pomodoro",
        tooltip_text: Utils.watch(getTooltip(), runTime, getTooltip),
        on_clicked: () => print(runTime.isPolling), // TODO: FIX - isPolling always false...
        on_secondary_click: () => initSec.value = 2700,

        child: Widget.Icon({
            icon: Utils.watch(getIcon(), runTime, getIcon)
        })
    })
}


// Volume Widget
function Speaker() {

    const icons = {
        67: "high",
        34: "medium",
        1: "low",
        0: "muted",
    }

    function getIcon() {
        const icon = audio.speaker.is_muted ? 0 : [67, 34, 1, 0].find(
            threshold => threshold <= audio.speaker.volume * 100)

        return `audio-volume-${icons[icon]}`
    }

    function getVolume() {
        return audio.speaker.is_muted ? 'mut' : `${Math.round(audio.speaker.volume * 100)}%`
    }

    const icon = Widget.Icon({
        icon: Utils.watch(getIcon(), audio.speaker, getIcon),
    })

    const volume = Widget.Label({
        label: Utils.watch(getVolume(), audio.speaker, getVolume),
    })

    return Widget.Box({
        spacing: 4,
        class_name: "speaker",
        children: [icon, volume],
    })
}


// Microphone Widget
function Microphone() {

    const icons = {
        67: "high",
        34: "medium",
        1: "low",
        0: "muted",
    }

    function getIcon() {
        const icon = audio.microphone.is_muted ? 0 : [67, 34, 1, 0].find(
            threshold => threshold <= audio.microphone.volume * 100)

        return `mic-volume-${icons[icon]}`
    }

    function getVolume() {
        return audio.microphone.is_muted ? 'mut' : `${Math.round(audio.microphone.volume * 100)}%`
    }

    const icon = Widget.Icon({
        icon: Utils.watch(getIcon(), audio.microphone, getIcon),
    })

    const volume = Widget.Label({
        label: Utils.watch(getVolume(), audio.microphone, getVolume),
    })

    return Widget.Box({
        spacing: 4,
        class_name: "microphone",
        children: [icon, volume],
    })
}


// Audio Widget
function Audio() {

    return Widget.Button({
        // cursor: "pointer".
        class_name: "audio",
        on_clicked: () => hyprland.messageAsync("dispatch exec [floating] pavucontrol"),
        child: Widget.Box({
            spacing: 8,
            children: [Speaker(), Microphone()],
        })
    })
}


// Network Widget
function Network() {

    function getInternet() {
        return network.primary ? ` ${network[network.primary].internet.charAt(0).toUpperCase() + network[network.primary].internet.slice(1)} ` : " No Connection Found "
    }

    function getIcon() {
        switch (network.primary) {
            case "wifi":
                return network.wifi.icon_name

            case "wired":
                // ! AGS's Network Service has some problems during
                // ! the new connection and I have no idea how to
                // ! fix this. `network.wired.internet` shows
                // ! 'disconnected' after connecting.
                // TODO: Post the issue on AGS repo.
                return "network-wired-symbolic"

            default:
                return "network-wired-offline-symbolic"
        }
    }

    return Widget.Button({
        // cursor: "pointer".
        class_name: "network",
        on_clicked: () => {
            print(network[network.primary].internet)
            print(network[network.primary].state)
            print(network[network.primary].icon_name)

            hyprland.messageAsync("dispatch exec [floating] nm-connection-editor")
        },
        tooltip_text: Utils.watch(getInternet(), network, getInternet), // Capiralized connection

        child: Widget.Icon({
            icon: Utils.watch(getIcon(), network, getIcon),
        }),
    })
}


// Bluetooth Widget
function Bluetooth() {

    function getIcon() {
        return bluetooth.enabled ? "bluetooth-active-symbolic" : "bluetooth-disconnected-symbolic"
    }

    return Widget.Button({
        // cursor: "pointer",
        class_name: "bluetooth",
        on_clicked: () => hyprland.messageAsync("dispatch exec [floating] blueman-manager"),

        child: Widget.Icon({
            icon: Utils.watch(getIcon(), bluetooth, getIcon),
        })
    })
}

// Battery Widget
function Battery() {

    const value = battery.bind("percent")

    const charging = battery.bind("charging")

    const icon = battery.bind("percent")
        .as(p => `battery-level-${Math.floor(p / 10) * 10}${charging ? "-charging" : ""}-symbolic`)

    const currEnergy = Math.floor(battery.bind("energy") * 10) / 10

    const fullEnergy = Math.floor(battery.bind("energy-full") * 10) / 10

    const rateEnergy = Math.floor(battery.bind("energy-rate") * 10) / 10

    return Widget.Button({
        class_name: "battery",
        visible: battery.bind("available"),
        on_clicked: () => print(icon),
        tooltip_text: ` ${currEnergy}/${fullEnergy} Watt \n Drain: ${rateEnergy} Watt `,

        child: Widget.Box({
            spacing: 4,
            children: [
                Widget.Icon({ icon: icon }),
                Widget.Label({ label: `${value}%` }),
            ],
        }),
    })
}


// Clock Widget
function Clock() {

    const date = Variable('', {
        poll: [1000, 'date +"%b %e, %H:%M"']
    })

    return Widget.Button({
        // cursor: "pointer".
        class_name: "clock",
        on_hover: () => calendarVisible.value = true,
        on_hover_lost: () => calendarVisible.value = false,
        child: Widget.Label({ label: date.bind() }),
    })
}


// BAR LAYOUT
function Left() {

    return Widget.Box({
        class_name: "left",
        children: [
            Widget.Label({
                // Proprietary Archlinux logo B-)
                class_name: "distro",
                label: "󰣇",
            }),
            Workspaces(),
        ],
    })
}

function Center() {

    return Widget.Box({
        class_name: "middle",
        spacing: 4,
        children: [
            Widget.Label({ label: "😎" }),
            // Media(),
            Notifications(),
        ],
    })
}

function Right() {

    return Widget.Box({
        class_name: "right",
        hpack: "end",
        children: [
            SysTray(),
            Pomodoro(),
            Audio(),
            Network(),
            Bluetooth(),
            Battery(),
            Clock(),
        ],
    })
}


// BAR
function Bar(monitor = 0) {

    return Widget.Window({
        name: `bar-${monitor}`, // name has to be unique
        monitor,
        anchor: ["top", "left", "right"],
        exclusivity: "exclusive",
        layer: "background",

        child: Widget.CenterBox({
            class_name: "bar",
            start_widget: Left(),
            center_widget: Center(),
            end_widget: Right(),
        }),
    })
}


// Status Widget
function Status() {

    function getStatus() {
        return JSON.parse(Utils.exec(App.configDir + '/scripts/getStatus.sh'))
    }

    const status = Variable(getStatus(), {
        poll: [2000, getStatus]
    })

    // Stop the poll after the first iteration
    status.stopPoll()

    // Depending on calendarVisible
    calendarVisible.connect('changed', v => {
        // If calebdar is visible,
        v.value ?
            // resume the poll if not running
            !status.bind().isPolling && status.startPoll() :
            // else stop the poll if running
            status.stopPoll()
    })

    return [
        // CPU %   RAM %   GPU %
        Widget.CenterBox({
            class_name: "status-top",
            start_widget: Widget.Box({
                vertical: true,
                children: status.bind().as(v => [
                    Widget.CircularProgress({
                        class_name: "circular-progress",
                        css: `color: ${v["cpu_usage"].color};`,
                        start_at: 0.75,
                        value: v["cpu_usage"].value / 100,
                        child: Widget.Label({
                            css: "font-size: 16px;",
                            label: "CPU",
                        }),
                    }),
                    Widget.Label({
                        class_name: "status-label",
                        justification: "center",
                        label: `${v["cpu_usage"].value}%`
                    })
                ])
            }),
            center_widget: Widget.Box({
                vertical: true,
                children: status.bind().as(v => [
                    Widget.CircularProgress({
                        class_name: "circular-progress",
                        css: `color: ${v["ram_usage"].color};`,
                        start_at: 0.75,
                        value: v["ram_usage"].value / 100,
                        child: Widget.Label({
                            css: "font-size: 16px;",
                            label: "RAM",
                        }),
                    }),
                    Widget.Label({
                        class_name: "status-label",
                        justification: "center",
                        label: `${v["ram_usage"].value}%`
                    })
                ])
            }),
            end_widget: Widget.Box({
                vertical: true,
                children: status.bind().as(v => [
                    Widget.CircularProgress({
                        class_name: "circular-progress",
                        css: `color: ${v["gpu_usage"].color};`,
                        start_at: 0.75,
                        value: v["gpu_usage"].value / 100,
                        child: Widget.Label({
                            css: "font-size: 16px;",
                            label: "GPU",
                        }),
                    }),
                    Widget.Label({
                        class_name: "status-label",
                        justification: "center",
                        label: `${v["gpu_usage"].value}%`
                    })
                ])
            }),
        }),

        // CPUC   DSK %   GPUC
        Widget.CenterBox({
            class_name: "status-bottom",
            start_widget: Widget.Box({
                vertical: true,
                children: status.bind().as(v => [
                    Widget.CircularProgress({
                        class_name: "circular-progress",
                        css: `color: ${v["cpu_temp"].color};`,
                        start_at: 0.75,
                        value: v["cpu_temp"].value / 100,
                        child: Widget.Label({
                            css: "font-size: 16px;",
                            label: "CPU",
                        }),
                    }),
                    Widget.Label({
                        class_name: "status-label",
                        justification: "center",
                        label: `${v["cpu_temp"].value}C`
                    })
                ])
            }),
            center_widget: Widget.Box({
                vertical: true,
                children: status.bind().as(v => [
                    Widget.CircularProgress({
                        class_name: "circular-progress",
                        css: `color: ${v["disk_usage"].color};`,
                        start_at: 0.75,
                        value: v["disk_usage"].value / 100,
                        child: Widget.Label({
                            css: "font-size: 16px;",
                            label: "SDA",
                        }),
                    }),
                    Widget.Label({
                        class_name: "status-label",
                        justification: "center",
                        label: `${v["disk_usage"].value}%`
                    })
                ])
            }),
            end_widget: Widget.Box({
                vertical: true,
                children: status.bind().as(v => [
                    Widget.CircularProgress({
                        class_name: "circular-progress",
                        css: `color: ${v["gpu_temp"].color};`,
                        start_at: 0.75,
                        value: v["gpu_temp"].value / 100,
                        child: Widget.Label({
                            css: "font-size: 16px;",
                            label: "GPU",
                        }),
                    }),
                    Widget.Label({
                        class_name: "status-label",
                        justification: "center",
                        label: `${v["gpu_temp"].value}C`
                    })
                ])
            }),
        })
    ]
}


// Calendar Widget
const calendar = Widget.Calendar({

    class_name: "calendar",
    // cursor: "pointer".
    sensitive: false,

    showDayNames: true,
    showDetails: false,
    showHeading: true,
    showWeekNumbers: false,
})


// Calendar Wrapper
function CalendarWrapper() {

    const wrapper = Widget.EventBox({
        child: Widget.Box({
            class_name: "calendarbox",
            vertical: true,
            children: [
                calendar,
                ...Status(),
            ]
        })
    })

    // A workaround for calendarVisible to work :/
    wrapper.connect('leave-notify-event', () => {
        calendarVisible.value = false
    })

    return wrapper
}


// CALENDAR
function Calendar(monitor = 0) {

    return Widget.Window({
        visible: calendarVisible.bind(),
        name: `calendar-${monitor}`,
        monitor,
        anchor: ["top", "right"],
        exclusivity: "normal",
        layer: "top",
        child: CalendarWrapper(),
    })
}


// APP
App.config({
    style: "./style.css",
    windows: [
        Bar(),
        Calendar(),

        // you can call it, for each monitor
        // Bar(0),
        // Bar(1)
    ],
})
class Pomodoro extends Service {
    static {
        Service.register(
            this,
            {
                'stopped': [],
                'resumed': [],
                'restarted': [],
                'tick': ['float'], // Signal for countdown updates
            },
            {
                'running': ['bool', 'rw'], // Indicates if the countdown is running
                'seconds': ['float', 'rw'],  // Current seconds remaining
                'bind': [],
            },
        );
    }

    #initialSeconds;
    #currentSeconds;
    #timerId;
    #running = false;

    get running() {
        return this.#running;
    }

    set running(value) {
        if (value && !this.#running) {
            this.start();
        } else if (!value && this.#running) {
            this.stop();
        }
    }

    get initSeconds() {
        return this.#initialSeconds;
    }

    get seconds() {
        return this.#currentSeconds;
    }

    set seconds(value) {
        this.#initialSeconds = value;
        this.#currentSeconds = value;
        this.emit('restarted');
        this.emit('tick', this.#currentSeconds);
    }

    constructor(initialSeconds) {
        super();
        this.#initialSeconds = initialSeconds;
        this.#currentSeconds = initialSeconds;
        this.#running = false;
        this.#timerId = null;
    }

    #tick() {
        this.#currentSeconds--;
        this.emit('tick', this.#currentSeconds);

        if (this.#currentSeconds <= 0) {
            this.stop();
            Utils.exec(App.configDir + '/scripts/pomodoroEnd.sh')
        }
    }

    start() {
        if (this.#currentSeconds <= 0) {
            this.emit('restarted');
            this.#currentSeconds = this.#initialSeconds
        }

        if (!this.#running) {
            this.#running = true;
            this.emit('resumed');
            this.#timerId = setInterval(() => this.#tick(), 1000);
        }
    }

    stop() {
        if (this.#running) {
            clearInterval(this.#timerId);
            this.#timerId = null;
            this.#running = false;
            this.emit('stopped');
        }
    }

    connect(event = 'changed', callback) {
        return super.connect(event, callback);
    }

    bind(prop = 'seconds') {
        return super.bind(this, prop)
    }
}

const pomodoro = new Pomodoro(2700); // 45 minutes in seconds

export default pomodoro;

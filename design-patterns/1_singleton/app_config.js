class AppConfig {
  constructor() {
    if (AppConfig.instance) {
      return AppConfig.instance;
    }
    AppConfig.instance = this;
  }
}

const config1 = new AppConfig();
const config2 = new AppConfig();

console.log(config1 === config2); // true

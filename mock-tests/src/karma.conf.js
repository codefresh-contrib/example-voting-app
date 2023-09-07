module.exports = function (config) {
    config.set({
      basePath: '',
      frameworks: ['jasmine', '@angular-devkit/build-angular'],
      plugins: [
        require('karma-jasmine'),
        require('karma-chrome-launcher'),
        require('karma-jasmine-html-reporter'),
        require('karma-allure-reporter'),
        require('@angular-devkit/build-angular/plugins/karma')
      ],
      angularCli: {
        config: '../angular.json',
        environment: 'dev'
      },
      reporters: ['progress','allure'],
      port: 9876,
      colors: true,
      logLevel: config.LOG_INFO,
      watch: false,
      browsers: ['Chrome'],
      singleRun: true,
      allureReport: {
        reportDir: '../../allure-results',
        useBrowserName: true
      }
    });
}
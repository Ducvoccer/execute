const open = require('open');
fs = require('fs')

const dir_path = '/usr/games/notify_birthday';

(async () => {
    try {
        await open(dir_path + '/index.html', { app: ['google-chrome'] });
    } catch (e) {
        console.log('error is');
        console.log(e);
    }
})();

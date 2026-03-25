// 每次你更改 sw.js 、index.html 、 manifest.json时，就把这个版本号改一下（比如 v1 改成 v2）

const CACHE_NAME = 'power-station-v2'; 

const ASSETS = [

  './',

  './index.html',

  './manifest.json'

];



// 安装时强制跳过等待

self.addEventListener('install', e => {

  self.skipWaiting(); 

  e.waitUntil(

    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))

  );

});



// 激活时清理旧缓存

self.addEventListener('activate', e => {

  e.waitUntil(

    caches.keys().then(keys => Promise.all(

      keys.map(key => {

        if (key !== CACHE_NAME) return caches.delete(key);

      })

    ))

  );

});



// 策略：网络优先，报错则找缓存

self.addEventListener('fetch', e => {

  e.respondWith(

    fetch(e.request).catch(() => caches.match(e.request))

  );

});

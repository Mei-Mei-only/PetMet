const CACHE_NAME = 'petmet-cache-v1';
const urlsToCache = [
  '/',
  '/static/',
  '/static/PetMetLogo.jpg',
  '/static/TeamLogo.png',
  '/static/team/Arvin.png',
  '/static/team/455955679_1001877174954352_6720492336956922263_n.jpg',
  '/static/team/455700785_1038882434606928_3900257605003181516_n.jpg',
  '/static/team/bernalene.png',
  // Add other static files you want to cache
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});

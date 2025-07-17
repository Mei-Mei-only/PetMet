const CACHE_NAME = 'petmet-cache-v1';
const urlsToCache = [
  '/',
  './manifest.json',
  './PetMetLogo.jpg',
  './TeamLogo.png',
  './team/Arvin.png',
  './team/455955679_1001877174954352_6720492336956922263_n.jpg',
  './team/455700785_1038882434606928_3900257605003181516_n.jpg',
  './team/bernalene.png',
  // Add other static files you want to cache
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
});

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js', { scope: '/' })
      .then(registration => {
        console.log('SW registered with scope:', registration.scope);
      })
      .catch(err => {
        console.log('SW registration failed:', err);
      });
  });
}

let deferredPrompt;
const installBtn = document.getElementById('installBtn');

// Enhanced installation handling
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  if (installBtn) {
    installBtn.style.display = 'block';
    installBtn.addEventListener('click', async () => {
      if (!deferredPrompt) return;
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      console.log(outcome === 'accepted' ? 'Accepted' : 'Dismissed');
      deferredPrompt = null;
      if (installBtn) installBtn.style.display = 'none';
    });
  }
});

window.addEventListener('appinstalled', () => {
  console.log('PWA installed');
  if (installBtn) installBtn.style.display = 'none';
  trackInstallation();
});

function trackInstallation() {
  fetch('/track-pwa-install/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({type: 'install'})
  }).then(response => {
    console.log('Installation tracked');
    updateDownloadCount();
  });
}

function updateDownloadCount() {
  const counter = document.getElementById('pwa-stat');
  if (counter) {
    const current = parseInt(counter.textContent) || 0;
    counter.textContent = (current + 1) + '+';
  }
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

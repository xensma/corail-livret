// Utilitaire : transforme les URLs d'un texte en liens cliquables.
// Sûr : on échappe d'abord le HTML (le contenu vient des JSON édités via Sveltia).
// Les liens YouTube deviennent un libellé « ▶ Voir la vidéo ».

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export function linkify(text: string | undefined | null): string {
  if (!text) return '';
  const escaped = escapeHtml(String(text));
  return escaped.replace(/(https?:\/\/[^\s<]+)/g, (raw) => {
    const url = raw.replace(/[).,;:]+$/, ''); // retire la ponctuation finale collée à l'URL
    const isYouTube = /(?:youtube\.com|youtu\.be)/i.test(url);
    const label = isYouTube ? '▶ Voir la vidéo' : url;
    return `<a href="${url}" target="_blank" rel="noopener noreferrer" class="text-corail-turquoise-dark font-medium underline underline-offset-2 hover:text-corail-turquoise break-words">${label}</a>`;
  });
}

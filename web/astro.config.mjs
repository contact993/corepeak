// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';

// When a custom domain is connected later, set SITE to it and BASE to '/'.
const SITE = process.env.SITE_URL || 'https://contact993.github.io';
const BASE = process.env.BASE_PATH || '/pikaxps';

const softwareJsonLd = {
  '@context': 'https://schema.org',
  '@type': 'SoftwareApplication',
  name: 'PikaXPS',
  applicationCategory: 'ScienceApplication',
  operatingSystem: 'macOS, Windows',
  description:
    'Free, cross-platform XPS (X-ray photoelectron spectroscopy) peak-fitting app with a built-in fit auditor and a citation-backed reference database. The modern replacement for XPSPEAK 4.1.',
  url: SITE + BASE + '/',
  downloadUrl: 'https://github.com/contact993/pikaxps/releases',
  softwareVersion: '0.1.0',
  license: 'https://www.gnu.org/licenses/gpl-3.0.html',
  offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
  author: { '@type': 'Person', name: 'Pika' },
};

export default defineConfig({
  site: SITE,
  base: BASE,
  integrations: [
    sitemap(),
    starlight({
      title: 'PikaXPS',
      tagline: 'Free XPS peak fitting for Mac & Windows — with a built-in fit auditor',
      description:
        'Free, cross-platform XPS peak-fitting software with a fit auditor and a citation-backed reference database. The modern XPSPEAK 4.1 replacement.',
      social: { github: 'https://github.com/contact993/pikaxps' },
      favicon: '/favicon.svg',
      customCss: ['./src/styles/custom.css'],
      defaultLocale: 'root',
      locales: {
        root: { label: 'English', lang: 'en' },
        ko: { label: '한국어', lang: 'ko' },
      },
      components: {
        Footer: './src/components/Footer.astro',
      },
      head: [
        {
          tag: 'meta',
          attrs: { name: 'google-site-verification', content: 'Jb7_bS0AuF37HAY96022zna0kUWMYkEee1z8YZSFsSY' },
        },
        {
          tag: 'script',
          attrs: { async: true, src: 'https://www.googletagmanager.com/gtag/js?id=G-3F1GD0CKKM' },
        },
        {
          tag: 'script',
          content:
            "window.dataLayer = window.dataLayer || [];\n" +
            "function gtag(){dataLayer.push(arguments);}\n" +
            "gtag('js', new Date());\n" +
            "gtag('config', 'G-3F1GD0CKKM');",
        },
        {
          tag: 'script',
          attrs: { type: 'application/ld+json' },
          content: JSON.stringify(softwareJsonLd),
        },
        // Social / Open Graph image (helps link previews drive traffic)
        { tag: 'meta', attrs: { property: 'og:image', content: SITE + BASE + '/screenshot.png' } },
        { tag: 'meta', attrs: { property: 'og:type', content: 'website' } },
        { tag: 'meta', attrs: { name: 'twitter:card', content: 'summary_large_image' } },
        { tag: 'meta', attrs: { name: 'twitter:image', content: SITE + BASE + '/screenshot.png' } },
        { tag: 'meta', attrs: { name: 'keywords', content: 'XPS, X-ray photoelectron spectroscopy, peak fitting, curve fitting, XPSPEAK alternative, CasaXPS alternative, free XPS software, surface analysis, Mac' } },
      ],
      sidebar: [
        { label: 'Download', translations: { ko: '다운로드' }, link: '/download/' },
        { label: 'Features', translations: { ko: '기능' }, link: '/features/' },
        { label: 'Compare', translations: { ko: '비교' }, link: '/compare/' },
        {
          label: 'Guides',
          translations: { ko: '가이드' },
          items: [
            { label: 'Shirley vs Tougaard background', link: '/guides/shirley-vs-tougaard/' },
            { label: 'Spin-orbit doublet fitting', link: '/guides/doublet-fitting/' },
            { label: 'The fit audit (BIC / leave-one-out)', link: '/guides/fit-audit/' },
          ],
        },
        { label: 'Cite', translations: { ko: '인용' }, link: '/cite/' },
        { label: 'Feedback', translations: { ko: '피드백·기능요청' }, link: '/feedback/' },
        { label: 'Contribute a reference', translations: { ko: '레퍼런스 제보' }, link: '/contribute/' },
      ],
    }),
  ],
});

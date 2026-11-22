# Laman Web Asia Berkat Enterprise

Laman satu halaman (statik) untuk **Asia Berkat Enterprise — Pusat Khidmat Telco**, Kelantan.
Tema ikut logo ABE: merah · hitam · perak. Mesra telefon, pantas (gambar WebP), sedia SEO.

## Maklumat perniagaan
- Dealer sah telco · SSM 202103037448 (003235634-V)
- 4 lokasi ikut SSM: Beris Jejawi (KB, ibu pejabat), Kemumin (KB), Machang, Gua Musang
- Waktu operasi: 9:00 pagi – 6:00 petang setiap hari, **tutup hari Jumaat**
- WhatsApp 017-380 5112 · Telefon 011-1066 3807, 019-495 4558 · TikTok @asiaberkat_1

## Kandungan laman
1. **Hero** — "Keperluan Telco Anda, Kami Bantu." + butang Hubungi Kami (WhatsApp) & Lihat Lokasi Kedai, logo, pakej hot Celcom, statistik, jalur logo telco.
2. **Pakej & Pelan** — Pakej telefon + pelan Celcom (RM279 muka / RM70 sebulan / 24 bulan), Unifi Mobile + Nubia A77 (RM59), CelcomDigi Power+ 55/65, jadual prabayar CelcomDigi Nov 2026, internet rumah U Home 5G. Butang *Poster* buka poster asal.
3. **Telefon 5G** — 8 model, setiap satu ada butang *Tanya Harga* (WhatsApp dengan nama model).
4. **Kami Bantu** — kelayakan, pelan, bajet, masalah line.
5. **Pelanggan Kami** — galeri gambar pelanggan (tekan untuk besarkan).
6. **3 Langkah**, **Lokasi** (4 kedai + peta + Google Maps/Waze), **Tentang**, **Soalan Lazim**, CTA, footer, butang WhatsApp terapung.

## Tukar maklumat
| Nak tukar | Di mana |
|---|---|
| Nombor WhatsApp | Cari `wa.me/60173805112` dalam `index.html` → ganti semua (Find & Replace). Juga dalam `404.html`, `llms.txt`. |
| Nombor telefon | Cari `017-380 5112` / `011-1066 3807` dan `tel:+60...` |
| Harga pakej | Bahagian `<!-- ============ PAKEJ ============ -->` dalam `index.html`, dan `llms.txt` |
| Gambar | Letak fail baharu dalam `assets/img/` (WebP disyorkan, nisbah 4:5) dan tukar nama fail dalam `index.html` |
| Soalan lazim | Dalam `index.html` (`<details>`) **dan** blok JSON-LD `FAQPage` di bahagian `<head>` — pastikan sama |
| Waktu operasi | Cari `9:00 pagi` dalam `index.html` (lokasi, Hubungi, Fakta, footer, Soalan Lazim) dan `openingHoursSpecification` dalam JSON-LD, serta `llms.txt` |
| Domain | Sudah ditetapkan `https://asiaberkat.my`. Jika bertukar, cari & ganti dalam `index.html`, `robots.txt`, `sitemap.xml`, `llms.txt` |

Selepas ubah CSS/JS, naikkan nombor `?v=20261122-2` dalam `index.html` supaya pelayar ambil versi baharu.

## Struktur fail
```
index.html          laman utama
css/style.css       gaya
js/main.js          menu, animasi, peta, lightbox
assets/img/         logo, gambar pelanggan, poster, logo telco, og-image.jpg
404.html, robots.txt, sitemap.xml, llms.txt, site.webmanifest, ikon
```

## Deploy (Netlify — percuma)
1. Pergi ke app.netlify.com → *Add new site* → *Import from Git* → pilih repo `Dynopos/Asiaberkat` (branch `main`, tiada build command, publish directory `/`). Setiap push ke `main` akan auto-deploy.
2. Sambung domain `asiaberkat.my` di *Domain settings* (tambah juga `www.asiaberkat.my`), kemudian ikut arahan DNS Netlify di pendaftar domain.
3. Selepas live: daftar di Google Search Console, hantar `sitemap.xml`, dan letak URL laman dalam Google Business Profile setiap cawangan.

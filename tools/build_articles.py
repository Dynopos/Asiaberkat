"""Jana halaman artikel Asia Berkat: /artikel/ + 3 artikel SEO.
Jalankan: python3 -I build_articles.py /home/user/asiaberkat
"""
import json, os, sys, html
from urllib.parse import quote

ROOT = sys.argv[1]
URL = 'https://asiaberkat.my'
DATE = '2026-11-22'
WA_NUM = '60173805112'
E = html.escape


def wa(msg):
    return f'https://wa.me/{WA_NUM}?text=' + quote(msg)


ARTICLES = [
  {
    'slug': 'telco-paling-bagus-kota-bharu',
    'kw': 'telco paling bagus Kota Bharu',
    'title': 'Telco Paling Bagus di Kota Bharu? Cara Pilih Line Ikut Kawasan, Kegunaan & Bajet (2026)',
    'h1': 'Telco Paling Bagus di Kota Bharu: Cara Pilih Line yang Betul untuk Anda',
    'desc': 'Cari telco paling bagus di Kota Bharu? Panduan Asia Berkat: 3 faktor penting (liputan, kegunaan, bajet), contoh pelan CelcomDigi & U Mobile, dan cara uji line sebelum langgan.',
    'img': 'c-honor500smart', 'img_alt': 'Pelanggan Asia Berkat di kaunter kedai telco Kota Bharu dengan telefon Honor 500 Smart',
    'card': 'Tiada satu telco terbaik untuk semua orang. Ini 3 faktor yang menentukan line paling bagus untuk anda di Kota Bharu.',
    'body': '''
<p class="art__lead">Soalan paling kerap kami terima di kaunter Asia Berkat, Kota Bharu: <strong>"Telco mana paling bagus?"</strong> Jawapan jujurnya — <strong>tiada satu telco yang terbaik untuk semua orang</strong>. Line yang laju di Jalan Sultanah Zainab belum tentu sama kuat di rumah anda di Pengkalan Chepa atau Kubang Kerian. Yang paling bagus ialah telco yang padan dengan <em>tempat</em> anda guna telefon, <em>cara</em> anda guna, dan <em>bajet</em> anda.</p>

<h2 id="faktor-1">Faktor 1: Liputan di tempat anda paling kerap berada</h2>
<p>Liputan rangkaian berbeza ikut kawasan, malah ikut bangunan. Isyarat di luar rumah mungkin penuh, tetapi lemah di dalam bilik atau di tingkat bawah kedai. Sebelum pilih telco, fikirkan tiga lokasi utama anda:</p>
<ul>
  <li><strong>Rumah</strong> — tempat anda guna data paling banyak (YouTube, TikTok, panggilan video).</li>
  <li><strong>Tempat kerja / sekolah</strong> — penting untuk panggilan dan WhatsApp.</li>
  <li><strong>Laluan harian</strong> — contohnya jalan ke Pasir Mas, Tumpat atau Rantau Panjang.</li>
</ul>
<p><strong>Cara uji liputan sebelum langgan:</strong></p>
<ol>
  <li>Tanya jiran atau rakan sekerja telco apa yang mereka guna dan bagaimana isyaratnya di dalam bangunan.</li>
  <li>Semak peta liputan rasmi di laman web telco (contohnya <a href="https://www.u.com.my/en/personal/support/coverage-map" target="_blank" rel="noopener">peta liputan U Mobile</a>).</li>
  <li>Cuba dahulu dengan <strong>simkad prabayar</strong> — murah, tiada kontrak, boleh guna seminggu dua untuk uji.</li>
  <li>Untuk telefon yang menyokong eSIM, U Mobile ada <strong>ULTRA5G Trial percuma</strong>: 10GB data + panggilan tempatan tanpa had selama 7 hari.</li>
</ol>

<h2 id="faktor-2">Faktor 2: Cara anda guna telefon</h2>
<p>Pelan yang "paling bagus" untuk pelajar berbeza dengan pelan untuk peniaga online atau keluarga. Ini panduan ringkas berdasarkan pelan yang kami uruskan (harga Nov 2026):</p>
<div class="art__table"><table>
  <thead><tr><th>Jenis pengguna</th><th>Contoh pelan</th><th>Harga</th></tr></thead>
  <tbody>
    <tr><td>Guna ringan (WhatsApp, Facebook)</td><td>CelcomDigi 5G Hyper 30 — 50GB, prabayar</td><td>RM30 / 30 hari</td></tr>
    <tr><td>Data berat (video, hotspot)</td><td>CelcomDigi 5G Power 45 — tanpa had (FUP 250GB)</td><td>RM45 / 30 hari</td></tr>
    <tr><td>Kerap ke Thailand / Singapura</td><td>CelcomDigi 5G Power+ 55 / 65 — perantauan tanpa had SG, ID &amp; TH</td><td>RM55 / RM65</td></tr>
    <tr><td>Nak telefon baharu sekali</td><td>U Mobile ULTRA Postpaid 68 — 1,000GB + telefon 5G RM0</td><td>RM68 / bulan</td></tr>
    <tr><td>Keluarga (4 orang)</td><td>U Mobile ULTRA Family 128 — 4 talian, 1,000GB dikongsi</td><td>RM128 / bulan</td></tr>
  </tbody>
</table></div>
<p>Tinggal dekat sempadan seperti Rantau Panjang atau Pengkalan Kubor dan kerap ke Thailand? Pilih pelan yang ada <strong>perantauan Thailand</strong> — elak bil mengejut.</p>

<h2 id="faktor-3">Faktor 3: Bajet dan kelayakan</h2>
<ul>
  <li><strong>Prabayar</strong> — tiada semakan kelayakan, kawal belanja, sesuai untuk cuba-cuba.</li>
  <li><strong>Pascabayar</strong> — biasanya lebih banyak data untuk harga sama dan boleh "claim" telefon melalui pelan, tetapi tertakluk kepada semakan kelayakan telco.</li>
  <li><strong>Pakej telefon + pelan</strong> — contohnya pakej Celcom Plan 100 (1,000GB) dengan HONOR 600S: bayaran muka RM100 dan RM80 sebulan untuk 10 bulan pertama (kontrak 24 bulan), atau Unifi Mobile + Nubia A77 RM59 sebulan + SST.</li>
</ul>
<p>Pernah ditolak kelayakan? Jangan putus asa — ada pilihan dengan bayaran pendahuluan. Staf kami boleh bantu semak. Lihat juga <a href="../../#celcomdigi">senarai pakej telefon Celcom &amp; Digi</a>.</p>

<h2 id="telco-di-kota-bharu">Telco yang boleh anda urus di Kota Bharu</h2>
<p>Di dua cawangan Asia Berkat di Kota Bharu, anda boleh urus <strong>9 rangkaian</strong> di satu kaunter: Celcom, Digi, Maxis, Hotlink, U Mobile, Unifi Mobile, Tune Talk, XOX dan redONE. Jadi anda boleh bandingkan pilihan secara terus tanpa perlu ke banyak kedai.</p>
<ul>
  <li><strong>Beris Jejawi</strong> — Lot 403, Kg Beris Jejawi, Jalan Padang Tembak, Taman Orkid, 16100 Kota Bharu</li>
  <li><strong>Kemumin</strong> — Lot 1902-2, Kampung Kemumin, Jalan Sultanah Zainab II, 16100 Kota Bharu</li>
</ul>
<p>Buka setiap hari 9:00 pagi – 6:00 petang, kecuali hari Jumaat.</p>

<h2 id="langkah">5 langkah pilih telco paling bagus untuk anda</h2>
<ol>
  <li>Senaraikan lokasi utama anda (rumah, kerja, laluan harian).</li>
  <li>Tanya pengalaman jiran dan semak peta liputan.</li>
  <li>Uji dengan prabayar atau trial percuma sebelum ambil kontrak.</li>
  <li>Kira berapa data yang anda guna sebulan (lihat di <em>Tetapan → Data mudah alih</em>).</li>
  <li>Bandingkan pelan dan pakej telefon di satu tempat — kemudian baru buat keputusan.</li>
</ol>
''',
    'faq': [
      ('Telco mana paling bagus di Kota Bharu?', 'Tiada satu telco yang terbaik untuk semua orang. Telco paling bagus ialah yang liputannya kuat di rumah dan tempat kerja anda, sesuai dengan cara anda guna data, dan dalam bajet. Cara terbaik ialah uji dahulu dengan prabayar atau trial percuma.'),
      ('Bagaimana nak uji liputan sebelum langgan pascabayar?', 'Tanya jiran, semak peta liputan rasmi telco, dan cuba simkad prabayar selama seminggu dua. Bagi telefon eSIM, U Mobile menawarkan ULTRA5G Trial percuma 10GB selama 7 hari.'),
      ('Boleh tukar telco tanpa tukar nombor?', 'Boleh, melalui pindah nombor (port-in). Nombor anda kekal sama. Sesetengah telco memberi insentif — contohnya U Mobile memberi rebat port-in RM120 dan diskaun RM10 selama 12 bulan untuk pelan tertentu.'),
      ('Di mana nak urus line telefon di Kota Bharu?', 'Asia Berkat ada dua cawangan di Kota Bharu (Beris Jejawi dan Kemumin) yang menguruskan 9 rangkaian telco. Buka 9:00 pagi hingga 6:00 petang setiap hari kecuali Jumaat. WhatsApp 017-380 5112.'),
    ],
  },
  {
    'slug': 'telco-pilihan-kelantan',
    'kw': 'telco pilihan Kelantan',
    'title': 'Telco Pilihan Kelantan 2026: Perbandingan Pelan CelcomDigi, U Mobile & Unifi Mobile',
    'h1': 'Telco Pilihan Kelantan: Perbandingan Pelan Prabayar, Pascabayar & Internet Rumah (Nov 2026)',
    'desc': 'Telco pilihan Kelantan 2026 — bandingkan pelan prabayar CelcomDigi, pascabayar U Mobile ULTRA5G, Unifi Mobile dan internet rumah 5G dalam satu jadual. Panduan Asia Berkat.',
    'img': 'c-oppoa6t-a', 'img_alt': 'Pelanggan Asia Berkat di Kelantan dengan telefon OPPO A6t baharu',
    'card': 'Jadual perbandingan pelan prabayar, pascabayar, pakej telefon dan internet rumah yang popular di Kelantan — harga Nov 2026.',
    'body': '''
<p class="art__lead">Di Kelantan, pilihan telco semakin banyak — dari telco besar hingga MVNO yang lebih murah. Untuk memudahkan, kami di <strong>Asia Berkat</strong> himpunkan pelan yang paling kerap dipilih pelanggan kami di Kota Bharu, Machang dan Gua Musang, dalam satu tempat. Semua harga di bawah seperti diiklankan telco pada <strong>November 2026</strong>.</p>

<h2 id="prabayar">Prabayar: CelcomDigi 5G</h2>
<p>Sesuai untuk yang mahu kawal belanja, tiada kontrak dan tiada semakan kelayakan. Semua pelan sah 30 hari dengan panggilan tanpa had.</p>
<div class="art__table"><table>
  <thead><tr><th>Pelan</th><th>Data</th><th>Harga</th></tr></thead>
  <tbody>
    <tr><td>5G Hyper 30</td><td>50GB + hotspot</td><td>RM30</td></tr>
    <tr><td>5G Hyper 35</td><td>150GB + hotspot</td><td>RM35</td></tr>
    <tr><td>5G Power 35</td><td>Tanpa had (FUP 150GB), 18Mbps</td><td>RM35</td></tr>
    <tr><td>5G Power 45</td><td>Tanpa had (FUP 250GB), 48Mbps</td><td>RM45</td></tr>
    <tr><td>5G Power+ 55</td><td>Tanpa had (FUP 400GB), perantauan SG/ID/TH, Viu</td><td>RM55</td></tr>
    <tr><td>5G Power+ 65</td><td>Tanpa had (FUP 400GB), perantauan SG/ID/TH, Prime Video</td><td>RM65</td></tr>
  </tbody>
</table></div>

<h2 id="pascabayar">Pascabayar: U Mobile ULTRA5G (dengan telefon RM0)</h2>
<p>Pilihan popular untuk yang mahu <strong>"claim phone melalui plan"</strong> — telefon 5G RM0 bila langgan pelan tertentu (tertakluk kelayakan).</p>
<div class="art__table"><table>
  <thead><tr><th>Pelan</th><th>Kelebihan</th><th>Harga</th></tr></thead>
  <tbody>
    <tr><td>ULTRA Postpaid 45</td><td>500GB data &amp; hotspot</td><td>RM45/bln</td></tr>
    <tr><td>ULTRA Postpaid 68</td><td>1,000GB, roaming SG/ID/TH 15GB; telefon RM0 cth. Galaxy A07, Vivo Y11, realme C100</td><td>RM68/bln</td></tr>
    <tr><td>ULTRA Global 98</td><td>1,000GB, roaming 60+ destinasi; telefon RM0 cth. OPPO A6, HONOR 600S, Redmi Note 17 Pro</td><td>RM98/bln</td></tr>
    <tr><td>ULTRA Family 128</td><td>4 talian, 1,000GB dikongsi; telefon RM0 cth. Galaxy A57, Xiaomi 17T, atau 2 telefon RM0</td><td>RM128/bln</td></tr>
  </tbody>
</table></div>

<h2 id="pakej-telefon">Pakej telefon + pelan lain</h2>
<ul>
  <li><strong>Celcom &amp; Digi (kontrak 2 tahun)</strong> — kedua-duanya kini bergabung sebagai CelcomDigi, tetapi pelan dan harga masih berbeza. Plan 100 (1,000GB + panggilan tanpa had) dan Plan 80 (600GB + Viu 12 bulan). Contoh: HONOR 600S muka RM100, Celcom RM80 / Digi RM90 sebulan; nubia V80 Max (4G) muka RM160, Celcom RM59 / Digi RM67 sebulan (bulanan untuk 10 bulan pertama). <a href="../../#celcomdigi">Lihat semua 11 pilihan telefon</a>. Ada isu kelayakan? Kami bantu semak pilihan.</li>
  <li><strong>Unifi Mobile + Nubia A77</strong> — RM59 sebulan + SST. Kelayakan hijau: RM0 pendahuluan. Kelayakan merah: pendahuluan RM180, bulanan RM51.50 + SST selama 24 bulan.</li>
</ul>

<h2 id="internet-rumah">Internet rumah tanpa kabel</h2>
<p>Ramai rumah di Kelantan belum ada talian fiber. <strong>U Mobile ULTRA Home 5G</strong> jadi pilihan kerana tak perlu pasang kabel — cuma router 5G:</p>
<ul>
  <li>ULTRA Home 5G — RM68 sebulan (asal RM78), 1,000GB FUP, router WiFi 6 percuma.</li>
  <li>ULTRA Home 5G Pro — RM98 sebulan, 2,000GB FUP, router WiFi 7 dan AI Game Turbo.</li>
</ul>
<p>Pastikan rumah anda dalam kawasan liputan dahulu — <a href="../../#internet">lihat butiran internet rumah</a>.</p>

<h2 id="ikut-situasi">Telco pilihan ikut situasi</h2>
<ul>
  <li><strong>Pelajar / bajet ketat</strong> → prabayar RM30–RM35.</li>
  <li><strong>Peniaga online, banyak hotspot</strong> → Power 45 prabayar atau ULTRA Postpaid 68.</li>
  <li><strong>Kerap ke Thailand</strong> → Power+ 55/65 atau ULTRA Postpaid 68 (roaming TH disertakan).</li>
  <li><strong>Nak telefon baharu tanpa bayar penuh</strong> → pakej Celcom, Unifi Mobile, atau telefon RM0 U Mobile.</li>
  <li><strong>Satu keluarga</strong> → ULTRA Family 128 (4 talian).</li>
  <li><strong>Mahu lebih murah lagi</strong> → tanya pilihan MVNO seperti Tune Talk, XOX dan redONE yang menumpang rangkaian telco besar.</li>
</ul>

<h2 id="pindah">Nak tukar telco tapi kekal nombor?</h2>
<p>Gunakan <strong>pindah nombor (port-in)</strong> — nombor anda kekal. Bawa MyKad ke kedai kami, kami bantu uruskan. Untuk U Mobile, port-in ke ULTRA Family atau ULTRA Postpaid layak rebat RM120 dan diskaun RM10 selama 12 bulan.</p>
''',
    'faq': [
      ('Apakah telco pilihan di Kelantan?', 'Bergantung pada kegunaan. Prabayar CelcomDigi sesuai untuk bajet dan kawalan belanja, U Mobile ULTRA5G pascabayar popular untuk claim telefon RM0, dan U Mobile ULTRA Home 5G dipilih untuk internet rumah tanpa kabel. Asia Berkat menguruskan 9 rangkaian supaya anda boleh bandingkan di satu tempat.'),
      ('Pelan prabayar paling murah dengan data banyak?', 'Antara pilihan Nov 2026: CelcomDigi 5G Hyper 35 (150GB, RM35) dan 5G Power 35 (tanpa had dengan FUP 150GB, RM35). Semua pelan sah 30 hari dengan panggilan tanpa had.'),
      ('Boleh dapat telefon percuma dengan pelan?', 'Boleh. Contohnya U Mobile ULTRA Postpaid 68 (RM68 sebulan) dengan telefon 5G RM0 seperti Samsung Galaxy A07, tertakluk kepada kelayakan dan stok.'),
      ('Ada internet rumah tanpa pasang kabel di Kelantan?', 'Ada. U Mobile ULTRA Home 5G dari RM68 sebulan menggunakan router 5G tanpa pemasangan kabel. Liputan perlu disemak dahulu ikut alamat rumah.'),
    ],
  },
  {
    'slug': 'line-phone-paling-ok-kelantan',
    'kw': 'line phone paling ok Kelantan',
    'title': 'Line Phone Paling OK di Kelantan? Panduan Kota Bharu, Machang & Gua Musang',
    'h1': 'Line Phone Paling OK di Kelantan: Panduan Ikut Kawasan & Cara Atasi Line Lemah',
    'desc': 'Line phone paling ok di Kelantan bergantung pada kawasan. Panduan untuk Kota Bharu, Machang & Gua Musang, tip atasi line lemah, dan bila patut tukar telco — oleh Asia Berkat.',
    'img': 'c-honor600s-b', 'img_alt': 'Pelanggan Asia Berkat dengan telefon Honor 600S dan simkad CelcomDigi',
    'card': 'Line lemah di rumah? Panduan ikut kawasan Kota Bharu, Machang dan Gua Musang, serta 7 tip sebelum tukar telco.',
    'body': '''
<p class="art__lead">"Line apa yang OK kat sini?" — soalan biasa dari pelanggan kami, terutama yang baru pindah ke Kelantan. Hakikatnya, <strong>line paling OK berbeza ikut kawasan</strong>. Bandar seperti Kota Bharu biasanya ada lebih banyak pilihan rangkaian yang kuat, manakala kawasan berbukit dan pedalaman seperti sebahagian Gua Musang memerlukan lebih berhati-hati sebelum memilih.</p>

<h2 id="kota-bharu">Kota Bharu: banyak pilihan, utamakan isyarat dalam bangunan</h2>
<p>Di kawasan bandar, kebanyakan telco utama mempunyai liputan 4G dan liputan 5G semakin meluas. Cabaran sebenar biasanya <strong>isyarat di dalam bangunan</strong> — rumah teres, kedai deret atau bilik di bahagian belakang. Jika anda kerap guna data di rumah, pertimbangkan juga <a href="../../#internet">internet rumah 5G</a> supaya semua ahli keluarga dapat WiFi.</p>

<h2 id="machang">Machang: uji di rumah dan di laluan harian</h2>
<p>Untuk kawasan pinggir bandar dan kampung di sekitar Machang, isyarat boleh berbeza antara pekan dan kampung. Uji line di rumah <em>dan</em> sepanjang laluan harian anda — contohnya jalan ke tempat kerja — sebelum ambil kontrak.</p>

<h2 id="gua-musang">Gua Musang: jangan terus ambil kontrak</h2>
<p>Kawasan berbukit, ladang dan petempatan pedalaman lebih mencabar untuk semua rangkaian. Nasihat kami:</p>
<ul>
  <li><strong>Cuba prabayar dahulu</strong> selama seminggu dua sebelum langgan pascabayar berkontrak.</li>
  <li>Tanya jiran setempat — pengalaman mereka paling tepat untuk kawasan anda.</li>
  <li>Jika telefon menyokong <strong>dual-SIM</strong>, guna dua rangkaian berbeza supaya ada sandaran bila satu line lemah.</li>
  <li>Untuk internet rumah, semak liputan ikut alamat sebelum mendaftar.</li>
</ul>

<h2 id="tip-line-lemah">7 tip sebelum salahkan telco</h2>
<p>Kadangkala masalah bukan pada rangkaian, tetapi pada tetapan telefon atau simkad. Cuba langkah ini dahulu:</p>
<ol>
  <li><strong>Mod kapal terbang</strong> — hidupkan 10 saat, kemudian matikan untuk sambung semula ke menara terdekat.</li>
  <li><strong>Mulakan semula telefon</strong>.</li>
  <li><strong>Semak mod rangkaian</strong> — pastikan ditetapkan kepada 5G/4G (auto), bukan 3G/2G sahaja.</li>
  <li><strong>Hidupkan VoLTE / panggilan 4G</strong> jika ada pilihan — kualiti panggilan biasanya lebih baik.</li>
  <li><strong>Kemas kini perisian telefon</strong>.</li>
  <li><strong>Semak simkad</strong> — simkad yang sangat lama atau rosak boleh menjejaskan isyarat; tukar simkad baharu dengan nombor sama.</li>
  <li><strong>Cuba simkad di telefon lain</strong> — untuk pastikan masalah pada line atau pada telefon.</li>
</ol>
<p>Tak pasti? Bawa telefon dan MyKad ke mana-mana cawangan Asia Berkat — staf kami bantu semak.</p>

<h2 id="bila-tukar">Bila patut tukar telco?</h2>
<ul>
  <li>Isyarat lemah di rumah atau tempat kerja walaupun sudah cuba semua tip di atas.</li>
  <li>Data selalu perlahan pada waktu biasa anda guna.</li>
  <li>Bil lebih mahal berbanding pelan lain dengan data yang sama atau lebih.</li>
</ul>
<p>Tukar telco <strong>tak perlu tukar nombor</strong> — gunakan pindah nombor (port-in). Sesetengah pelan juga datang dengan telefon 5G RM0, contohnya <a href="../../#umobile">U Mobile ULTRA Postpaid 68</a>.</p>

<h2 id="cawangan">Cawangan Asia Berkat di Kelantan</h2>
<ul>
  <li><strong>Kota Bharu (Beris Jejawi)</strong> — Lot 403, Kg Beris Jejawi, Jalan Padang Tembak, Taman Orkid</li>
  <li><strong>Kota Bharu (Kemumin)</strong> — Lot 1902-2, Kampung Kemumin, Jalan Sultanah Zainab II</li>
  <li><strong>Machang</strong> — Lot 2191A, Kg Desa Harapan, Kg Air Belaga</li>
  <li><strong>Gua Musang</strong> — No 11, RKT Kesedar Paloh 1</li>
</ul>
<p>Buka 9:00 pagi – 6:00 petang setiap hari, kecuali Jumaat.</p>
''',
    'faq': [
      ('Line phone mana paling OK di Kelantan?', 'Ia bergantung pada kawasan anda. Di bandar seperti Kota Bharu, kebanyakan telco utama mempunyai liputan baik, manakala di kawasan pedalaman seperti sebahagian Gua Musang, lebih baik uji dengan prabayar dahulu dan tanya pengalaman jiran sebelum langgan.'),
      ('Kenapa line saya lemah di dalam rumah?', 'Dinding dan struktur bangunan boleh melemahkan isyarat. Cuba mod kapal terbang, semak mod rangkaian 5G/4G, hidupkan VoLTE dan kemas kini telefon. Jika masih lemah, pertimbangkan telco lain atau internet rumah 5G.'),
      ('Perlu tukar nombor kalau tukar telco?', 'Tidak. Gunakan pindah nombor (port-in) dan nombor anda kekal sama. Bawa MyKad ke cawangan Asia Berkat untuk dibantu.'),
      ('Di mana kedai telco Asia Berkat di Kelantan?', 'Asia Berkat ada 4 cawangan: dua di Kota Bharu (Beris Jejawi dan Kemumin), satu di Machang (Kg Air Belaga) dan satu di Gua Musang (Kesedar Paloh 1). Buka 9:00 pagi hingga 6:00 petang setiap hari kecuali Jumaat.'),
    ],
  },
]

ICONS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M12 21s-7-6.2-7-11.5a7 7 0 1 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/></symbol>
</svg>'''


def head(title, desc, canon, rel, ld, og_img):
    return f'''<!doctype html>
<html lang="ms">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#ffffff">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canon}">
<meta name="geo.region" content="MY-03">
<meta name="geo.placename" content="Kota Bharu, Kelantan">
<meta property="og:type" content="article">
<meta property="og:locale" content="ms_MY">
<meta property="og:site_name" content="Asia Berkat Enterprise">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{rel}favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{rel}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap"></noscript>
<link rel="stylesheet" href="{rel}css/style.css?v=20261123-1">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1).replace('</', '<\\/')}
</script>
</head>
<body>
<a class="skip" href="#kandungan">Langkau ke kandungan</a>
{ICONS}
<header class="nav is-scrolled" id="nav">
  <div class="wrap nav__in">
    <a class="brand" href="{rel}" aria-label="Asia Berkat Enterprise — laman utama">
      <img class="brand__logo" src="{rel}assets/img/logo-160.webp" width="160" height="160" alt="">
      <span class="brand__txt">ASIA BERKAT<small>Pusat Khidmat Telco</small></span>
    </a>
    <nav class="menu" id="menu" aria-label="Menu utama">
      <a href="{rel}#internet">Internet Rumah</a>
      <a href="{rel}#pakej">Pakej</a>
      <a href="{rel}#umobile">U Mobile</a>
      <a href="{rel}#lokasi">Lokasi</a>
      <a href="{rel}artikel/">Artikel</a>
      <a class="btn btn--red menu__cta" href="{wa('Hai Asia Berkat, saya nak bertanya tentang urusan telco.')}" data-wa target="_blank" rel="noopener"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> WhatsApp Kami</a>
    </nav>
    <a class="btn btn--red nav__cta" href="{wa('Hai Asia Berkat, saya nak bertanya tentang urusan telco.')}" data-wa target="_blank" rel="noopener"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> WhatsApp</a>
    <button class="burger" id="burger" aria-label="Buka menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  </div>
</header>
'''


def foot(rel):
    return f'''
<footer class="foot">
  <div class="wrap foot__in">
    <div>
      <a class="brand" href="{rel}"><img class="brand__logo" src="{rel}assets/img/logo-160.webp" width="160" height="160" alt=""><span class="brand__txt">ASIA BERKAT<small>Pusat Khidmat Telco</small></span></a>
      <p class="muted foot__reg">Asia Berkat Enterprise · SSM 202103037448 (003235634-V)<br>Lot 403 Kg Beris Jejawi, Jalan Padang Tembak, Taman Orkid, 16100 Kota Bharu, Kelantan<br>Buka 9:00 pagi – 6:00 petang · Tutup hari Jumaat<br><a href="tel:+60173805112">017-380 5112</a> · <a href="tel:+601110663807">011-1066 3807</a> · <a href="tel:+60194954558">019-495 4558</a></p>
    </div>
    <nav class="foot__nav" aria-label="Pautan footer">
      <a href="{rel}#internet">Internet Rumah</a><a href="{rel}#pakej">Pakej</a><a href="{rel}#umobile">U Mobile</a><a href="{rel}#lokasi">Lokasi</a><a href="{rel}artikel/">Artikel</a>
    </nav>
    <a class="btn btn--red" href="{wa('Hai Asia Berkat, saya nak bertanya tentang urusan telco.')}" data-wa target="_blank" rel="noopener"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> WhatsApp Kami</a>
  </div>
  <p class="wrap foot__copy">© 2026 Asia Berkat Enterprise. Nama dan jenama telco adalah milik syarikat masing-masing.</p>
</footer>
<a class="fab" href="{wa('Hai Asia Berkat, saya nak bertanya tentang urusan telco.')}" data-wa target="_blank" rel="noopener" aria-label="WhatsApp Asia Berkat"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg></a>
<script>
(function(){{var b=document.getElementById('burger'),m=document.getElementById('menu');
b.addEventListener('click',function(){{var o=!m.classList.contains('is-open');m.classList.toggle('is-open',o);b.setAttribute('aria-expanded',String(o));}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{m.classList.remove('is-open');b.setAttribute('aria-expanded','false');}}}});}})();
</script>
</body>
</html>
'''


ORG = {'@type': 'Organization', '@id': URL + '/#perniagaan', 'name': 'Asia Berkat Enterprise', 'url': URL + '/', 'logo': URL + '/assets/img/logo-480.png'}

for a in ARTICLES:
    rel = '../../'
    canon = f'{URL}/artikel/{a["slug"]}/'
    img_abs = f'{URL}/assets/img/{a["img"]}-800.webp'
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Article', '@id': canon + '#artikel', 'headline': a['h1'], 'description': a['desc'], 'image': img_abs,
         'datePublished': DATE, 'dateModified': DATE, 'inLanguage': 'ms-MY', 'mainEntityOfPage': canon,
         'author': ORG, 'publisher': ORG, 'keywords': a['kw'], 'about': {'@id': URL + '/#perniagaan'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Utama', 'item': URL + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Artikel', 'item': URL + '/artikel/'},
            {'@type': 'ListItem', 'position': 3, 'name': a['h1'], 'item': canon}]},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': ans}} for q, ans in a['faq']]},
    ]}
    others = [o for o in ARTICLES if o is not a]
    faq_html = '\n'.join(f'<details><summary>{E(q)}</summary><p>{E(ans)}</p></details>' for q, ans in a['faq'])
    rel_html = '\n'.join(f'<a class="tile acard" href="../{o["slug"]}/"><span class="eyebrow">Artikel</span><b>{E(o["h1"])}</b><span class="acard__go">Baca →</span></a>' for o in others)
    page = head(a['title'], a['desc'], canon, rel, ld, img_abs) + f'''
<main id="kandungan" class="wrap art-wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{rel}">Utama</a><span>/</span><a href="../">Artikel</a><span>/</span><span aria-current="page">{E(a['kw'].capitalize())}</span></nav>
  <article class="art">
    <header class="art__head">
      <span class="eyebrow"><span class="dot"></span>Panduan Telco · Kelantan</span>
      <h1>{E(a['h1'])}</h1>
      <p class="art__meta">Oleh <strong>Asia Berkat Enterprise</strong> · Dikemas kini <time datetime="{DATE}">22 November 2026</time></p>
    </header>
    <figure class="art__img"><img src="{rel}assets/img/{a['img']}-800.webp" srcset="{rel}assets/img/{a['img']}-480.webp 480w, {rel}assets/img/{a['img']}-800.webp 800w" sizes="(min-width:800px) 760px, 100vw" width="800" height="1000" alt="{E(a['img_alt'])}" fetchpriority="high"><figcaption>{E(a['img_alt'])}</figcaption></figure>
    <div class="art__body">
{a['body']}
    </div>
    <aside class="art__cta">
      <div><span class="eyebrow">Masih keliru?</span><b>Tanya terus staf Asia Berkat</b><p>Kami bantu bandingkan 9 rangkaian telco dan semak kelayakan anda — percuma untuk bertanya.</p></div>
      <div class="art__cta-btns">
        <a class="btn btn--red btn--lg" href="{wa('Hai Asia Berkat, saya baca artikel ' + chr(34) + a['h1'] + chr(34) + ' dan nak bertanya.')}" data-wa target="_blank" rel="noopener"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> WhatsApp 017-380 5112</a>
        <a class="btn btn--line btn--lg" href="{rel}#lokasi"><svg class="ico" aria-hidden="true"><use href="#i-pin"/></svg> Lokasi Kedai</a>
      </div>
    </aside>
    <section class="art__faq" aria-labelledby="faq-h">
      <h2 id="faq-h">Soalan lazim</h2>
      <div class="faq">
{faq_html}
      </div>
    </section>
    <p class="art__note">Harga dan pelan seperti diiklankan oleh syarikat telco pada November 2026, tertakluk kepada perubahan, liputan dan semakan kelayakan. Sila sahkan dengan staf kami sebelum mendaftar.</p>
  </article>
  <section class="art__more" aria-labelledby="more-h">
    <h2 id="more-h">Artikel lain</h2>
    <div class="acards">
{rel_html}
    </div>
  </section>
</main>
''' + foot(rel)
    os.makedirs(f'{ROOT}/artikel/{a["slug"]}', exist_ok=True)
    open(f'{ROOT}/artikel/{a["slug"]}/index.html', 'w', encoding='utf-8').write(page)

# Halaman senarai /artikel/
rel = '../'
canon = URL + '/artikel/'
ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'CollectionPage', '@id': canon, 'url': canon, 'name': 'Artikel & Panduan Telco Kelantan — Asia Berkat', 'inLanguage': 'ms-MY', 'publisher': ORG,
     'hasPart': [{'@type': 'Article', 'headline': a['h1'], 'url': f'{URL}/artikel/{a["slug"]}/'} for a in ARTICLES]},
    {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Utama', 'item': URL + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Artikel', 'item': canon}]}]}
cards = '\n'.join(f'''<a class="tile acard acard--img" href="{a['slug']}/">
        <img src="../assets/img/{a['img']}-480.webp" width="480" height="600" alt="{E(a['img_alt'])}" loading="lazy">
        <div><span class="eyebrow">{E(a['kw'].capitalize())}</span><b>{E(a['h1'])}</b><p>{E(a['card'])}</p><span class="acard__go">Baca artikel →</span></div>
      </a>''' for a in ARTICLES)
page = head('Artikel & Panduan Telco Kelantan | Asia Berkat', 'Panduan telco untuk Kota Bharu dan Kelantan: telco paling bagus, perbandingan pelan, dan line phone paling OK ikut kawasan — oleh Asia Berkat Enterprise.', canon, rel, ld, URL + '/assets/img/og-image.jpg') + f'''
<main id="kandungan" class="wrap art-wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{rel}">Utama</a><span>/</span><span aria-current="page">Artikel</span></nav>
  <header class="art__head art__head--list">
    <span class="eyebrow"><span class="dot"></span>Artikel &amp; Panduan</span>
    <h1>Panduan telco untuk <em>Kota Bharu &amp; Kelantan.</em></h1>
    <p class="sub">Tip memilih line, perbandingan pelan terkini dan cara atasi line lemah — ditulis oleh staf Asia Berkat berdasarkan soalan pelanggan di kaunter kami.</p>
  </header>
  <div class="acards acards--list">
    {cards}
  </div>
</main>
''' + foot(rel)
open(f'{ROOT}/artikel/index.html', 'w', encoding='utf-8').write(page)

# Data untuk laman utama & sitemap
json.dump([{'slug': a['slug'], 'h1': a['h1'], 'kw': a['kw'], 'img': a['img'], 'img_alt': a['img_alt'], 'card': a['card']} for a in ARTICLES],
          open(os.path.dirname(os.path.abspath(__file__)) + '/articles.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('siap:', [a['slug'] for a in ARTICLES])

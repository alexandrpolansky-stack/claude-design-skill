---
title: Add breaks and lines to your content
updated: 2023-07-19 20:29:40Z
created: 2023-07-19 20:18:02Z
latitude: 50.07553810
longitude: 14.43780050
altitude: 0.0000
---

### HTML-CSS zaklad

**HTML** - znamená **HyperText Markup Language** = struktura a kontent, co stránká má = kostra člověka 
**CSS** - **Cascading style sheets** = vzhled stránky = vzhled člověka

<html>
  <head>
    <link rel="stylesheet" href="css/style.css" type="text/css">
  </head>
  <body>
    <h1>Hello! My name is Alex and there is some HTML!</h1>
  </body>
</html>
HTML kód vytvořil text, který jsme napsali do těla stránky, jako H1 (header1) a pak pomocí CSS definujeme header color - barvu, background-color - barvu pozadí, a font (pokud nechceme klasický); css vlastně definuje vzhled html

h1 {
    color: blue;
  background-color: yellow; 
    font-family: sans-serif;
}


Text bez **HTML**
*[chybějící obrázek: 66bd54543b46f85127e394a20a5bff94.png]*
Text napsaný pomocí HTML
*[chybějící obrázek: 231448caaac94653ccf91e1a3c07ce00.png]*
**Můžeme vidět, že se tady nachází více headeru a podheadru, který má vždy své tělo a paragraph <p>**

Text s HTML a CSS
*[chybějící obrázek: 6d63a5d20bbddb8bf665b5acd05c772a.png]*
**Přidámeli CSS můžeme vidět uprávy jako underline, Bold, změnu fontu či background color**


Cvičení 1:
*[chybějící obrázek: c74c1bf2b81a926fc5cfd081cdc74222.png]*

## Add breaks and lines to your content
Breaks lines jsou super, pokud chceme rozdělit dva texty hned pod sebou, ale nejsou to dva rozdílné paragraphy, třeba adresy jsou super příklad

<p>Seirfertova 37/565</p>
<p>Praha 3</p>

Tohle nedává smysl

Ale pokud použijeme
<p>
Seifertova 37/565 <br>
Praha 3
</p>

Vypadá to mnohem lépe

Pak tady máme ještě horizontal rules neboli <hr>, což nám přidá takovouhle hezkou čárku

Ukázka kódu:
*[chybějící obrázek: 80f35d2ed22237025b90e7b06027c42d.png]*

Class address
*[chybějící obrázek: 8540e67dabe79ced8b565fd61a41bf30.png]*

Výsledek
*[chybějící obrázek: a74b5f254cabc5a3f1a508c194499fc6.png]*

### Apply CSS to HTML

V html jsme především používali <> v CSS narozdíl od toho používáme {} psané pravý alt + B	

struktura vypadá takhle

h1 nebo pokud mluvíme o classe .název classy pokud o id #názevID {
	property: value;
}

h1{
	font-family: Helvetica;
	color: blue;
	background-color:yellow;
}

### Class and ID

Classa a ids jsou custom atributy, které můžeš přidat ke svému elementu, abychom je nějak označili

Class se nastavuje v tagu </h1 class="domeček">
ID je víceméně stejné jako class, ale ID může být použito pouze jednou nemůžeme mít 5x ID="byt jedna", nedávalo by to smysl, mezitím co class="domeček" může být použita na domeček 1-5






*[chybějící obrázek: 009fc7a42b5c5a7a2559f97185d82284.png]*


### Colors
Několik možností jak zapsat barvu
Color name - white
Hex code - #FFFFFF
RGB value - 255,255,255 = což se zapisuje jako rgb(255, 255, 255 )
HSL color = Hue Saturation Lightness= což se zapisuje jako hsl(149, 88%, 49%)

Vždycky musíme používat kombinace barev a barvy celkově, které dávají smysl. To znamená zvolit dostatečně kontrastní barevné kombinace, aby i lidé, kteří nevidí dobře mohli obsah jednoduše přečíst

### Content Creating


Stále platí, **že vzhled prodává** bez **HTML a CSS by byly weby nepřehledné bez základních grafických úprav**, tak jak bylo vidět na první fotce v minulém notu. H a C nám dává hned několik bodů proč ho používat
- **Lehčí na čtení**
- **Vyhledávače** - pokud něco hledáme, vidíme header - Wikipedia
	- Body - popis - Tohle je wikipedia nejrozáshlejší online učebnice
- Toto také zajištuje, jaký web se vám vyhledá, čím kvalitnější kód tím lepší šance pro zobrazení (+milion dalších faktorů) **Pokud HTML nebude lehce čitelné, vyhledávač nebude vědět co se stránkou dělat**

Struktura kódu HTML
*[chybějící obrázek: 57ee17761f68a983c438527fa67edda0.png]*
**bracket - opening tag - text - bracket - closing tag**


Cvičení 2
*[chybějící obrázek: 95697ceffeb84e4e4d9e59f72473f9a0.png]*


### Create headings


Headings vytváříme pomocí <h></h> a to od čísla 1-6 s tím, že 1 je největší a 6 je nejmenší

<h1>I'm an h1 heading!</h1>
<h2>I'm an h2 heading!</h2>
<h3>I'm an h3 heading!</h3>
<h4>I'm an h4 heading!</h4>
<h5>I'm an h5 heading!</h5>
<h6>I'm an h6 heading!</h6>

h1 je rezervováno pro page title. A neměl by se používát víckrát jak jednou, abychom nezmátli vyhledávače a vyhledávací nástroje.

Pokud bychom nevyužívali paragraphy text a chtěli bychom mít mezi texty mezeru, není to možné.
**Příklad**:

Text 1





Text 2
*[chybějící obrázek: f9a89bb8c6948b888df6c0ac7f3fd2b5.png]*


Příklad 2. správně psaného HTML kódu


<h1>Polar bear</h1>

<p>From Wikipedia, the free encyclopedia</p>

<p>The polar bear (Ursus maritimus) is a carnivorous bear whose native range lies largely within the Arctic Circle, encompassing the Arctic Ocean, its surrounding seas and surrounding land masses. It is a large bear, approximately the same size as the omnivorous Kodiak bear (Ursus arctos middendorffi).[3] A boar (adult male) weighs around 350–700 kg (772–1,543 lb),[4] while a sow (adult female) is about half that size. Although it is the sister species of the brown bear,[5] it has evolved to occupy a narrower ecological niche, with many body characteristics adapted for cold temperatures, for moving across snow, ice and open water, and for hunting seals, which make up most of its diet.[6] Although most polar bears are born on land, they spend most of their time on the sea ice. Their scientific name means "maritime bear" and derives from this fact. Polar bears hunt their preferred food of seals from the edge of sea ice, often living off fat reserves when no sea ice is present. Because of their dependence on the sea ice, polar bears are classified as marine mammals.[7]</p>

<p>Because of expected habitat loss caused by climate change, the polar bear is classified as a vulnerable species, and at least three of the nineteen polar bear subpopulations are currently in decline.[8] However, at least two of the nineteen subpopulations are currently increasing, while another six are considered stable.[9] For decades, large-scale hunting raised international concern for the future of the species, but populations rebounded after controls and quotas began to take effect.[10] For thousands of years, the polar bear has been a key figure in the material, spiritual, and cultural life of circumpolar peoples, and polar bears remain important in their cultures. Historically, the polar bear has also been known as the white bear.[11]</p>

<h2>Naming and etymology</h2>

<p>Constantine John Phipps was the first to describe the polar bear as a distinct species in 1774.[1] He chose the scientific name Ursus maritimus, the Latin for 'maritime bear',[12] due to the animal's native habitat. The Inuit refer to the animal as nanook (transliterated as nanuq in the Inupiat language).[13][14] The Yupik also refer to the bear as nanuuk in Siberian Yupik.[15] The bear is umka in the Chukchi language. In Russian, it is usually called бе́лый медве́дь (bélyj medvédj, the white bear), though an older word still in use is ошку́й (Oshkúj, which comes from the Komi oski, "bear").[16] In Quebec, the polar bear is referred to as ours blanc ("white bear") or ours polaire ("polar bear").[17] In the Norwegian-administered Svalbard archipelago, the polar bear is referred to as Isbjørn ("ice bear").</p>

<p>The polar bear was previously considered to be in its own genus, Thalarctos.[18] However, evidence of hybrids between polar bears and brown bears, and of the recent evolutionary divergence of the two species, does not support the establishment of this separate genus, and the accepted scientific name is now therefore Ursus maritimus, as Phipps originally proposed.[1]</p>



### Dekórování pomocí CSS

Nejdřív se musí postavit základy domu, aby se mohl dekorovat

Pomocí **CSS dekorujeme kostru HTML**, ale musíme to **specifikovat pomocí kódů**. Také můžeme nastavit rozvržení webu, například umístit určitou sekci na levou stranu stránky, určit velikost navigačního panelu, který se zobrazí v horní části webu nebo zobrazit více sekcí vedle sebe.

Identifikujeme jaký prvek HTML chce customizovat (header, fonter, paragraph)

Příklad:
p{
	color: blue;
	font-family: Times new roman;

}

vždy začíname brakery pomocí **ALT GR + B, každý řádek kódu musí být ukončen zobáčkem**

### Divs and spans


Divs se používá pro blockové elementy
Spans se používá pro inline elementy

Rychlá rekapitulace:block elementy se ve výchozím nastavení zobrazují na svých vlastních řádcích, což způsobuje zalomení řádků. Inline elements se zobrazují vedle sebe a nezpůsobují zalomení řádků.

Divs elemnty pro seskupení objektů dohromady. Podobně jako header, nav, aside, footer, section, figure, article, pokud ale text nezapadá do žádné z této kategorií používáme právě div


Příklad:
*[chybějící obrázek: f84243aef2780669870b435a7a8a713e.png]*

Ty dva řádky, které mají modré pozadí jsou udělané právě pomocí divu, jelikož nezapadjí do žádné z kategorií header, footer, nav, article, section,aside, figure

Takže kód pro toto vypadá následovně
<div>
        <p>Note: this is an editorial piece and does not reflect the official opinion of the Sun Journal.</p>
        <p>For more information about our editorial team, click <a href="#">here</a>.</p>
    </div>
	
	
Span se používá právě pro inline elementy, takže napříkald pokud chceme odlišit jenom dvě slova v textu. Kde potom pomocí css uprávíme sekci span aby například text byl žlutý

<p>Note: this is an editorial piece and does not reflect the official opinion of the <span>Sun Journal.</span></p>
### Fonty

Serif To je s těmi ocásky 
Sans Serif nemá ocásky
Monospace má od sebe stejnou vzádelnost v každém písmeni

Fonty nastavujeme jak

X{
	font-family: Calibri, sans-serif;  = sans  serif slouží jako záložní font

}


Neměli by se používat více jak 3 různé fonty pro stránku
Fonty, které používáme by měli být logicky nastavené, že pro seznam jedna použijeme stejný font jako pro sezma 2

3 různé způsoby zapisovaní
/* pixels */
h1 {
    font-size: 48px;
}

p {
    font-size: 18px;
}

/* ems */
h1 {
    font-size: 3em;
}

p {
    font-size: 1.125em;
}

/* percentages */
h1 {
    font-size: 300%;
}

p {
    font-size: 112.5%;
}


**line height** neboli řádkování
#code-of-conduct {
    line-height: 1.4em;
}

**letter spacing**
h2 {
    letter-spacing: 0.08em;
}

**word spacing**
#quote {
    word-spacing: 1.1em;
}

Font weight = bold/normal nebo číselnou hodnotu 400 normalní 700 bold
Font style = italic
Text-decoration underline, none, line-through
Text-transformation = uppercase, lowercase


a:visited { = linky budou filové pokud na ně klikneme
    color: #858C7B;
}


a:hover { = když najedeme na tlačítko, bude mít barvu černou, bcg zelenou a velká písmená
    color: #151814;
    background-color: #DFFFD6;
    text-transform: uppercase;
    font-weight: normal;


### Head

Většinou jsou v html struktuře dvě sekce head & body
body má v sobě vše co jsem se už naučili section, nav, article, footer, header, figure, aside


Head má v sobě informace o stránce
linky do CSS, případně java scriptu
meta data = Jedná se o data, která mají informační hodnotu o webové stránce, ale nejsou na první pohled vidět. Tato data se nacházejí v kódu HTML webové stránky, většinou mezi tagy <head> a </head> a slouží především jako informace pro roboty vyhledávačů. Mezi metadata patří například popis stránky nebo seznam klíčových slov.

metu zapisujeme takto <meta name="název mety" content="název contentu">

**meta charset** informuje o kódováním, ve kterém byl dokument vytvořen
**meta name a content** description a content obsahuje popisek stránky, tím nám napomáha ve výsledcích vyhledávaní
**meta viewport content="width=device-width, initial-scale=1"** Tento meta tag je důležitý pro responzivní weby, protože říká prohlížeči, jak má web zobrazit, tj. jak moc ho má roztáhnout na displeji. Podle něj vlastně prohlížeč pozná, že je web navržený jako responzivní.
**meta tag soc. sítí** tagy, které pomáhají soc. sítím pochopit obsah stránky
**meta google nontranslate** pokud si nepřejeme, aby se stránka automaticky překládala

V meta tagu taky zapisujeme link CSS neboli <link href="odkaz na css">


<head>
    <!-- GENERAL INFO -->
    <title>10 Fun Facts About Dogs</title>
    <meta charset="utf-8">
    <meta name="description" content="Dogs are incredible creatures. There may still be some facts you don't know about them!">
    
    <!-- LINKS TO CSS FILE ("STYLESHEET") AND SITE ICON -->
    <link href="css/style.css" type="text/css" rel="stylesheet">
    <link href="favicon.ico" type="image/x-icon" rel="shortcut icon" >
    
    <!-- FACEBOOK METADATA -->
    <meta property="og:image" content="https://dogsdogsdogs.com/images/dog.png">
    <meta property="og:description" content="Dogs are incredible creatures. There may still be some facts you don't know about them!">
    <meta property="og:title" content="10 Fun Facts About Dogs">
    
    <!-- TWITTER METADATA -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="10 Fun Facts About Dogs">
    <meta name="twitter:description" content="Dogs are incredible creatures. There may still be some facts you don't know about them!">
    <meta name="twitter:image" content="https://dogsdogsdogs.com/images/dog.png">
</head>

### Inserting in HTML

Obrázky do HTML přidáme pomocí elementu img a dodatečné atributy src (source). Src se dá buďto použít na link, kde už se obrázek nachází či případně na soubor, kde je uložený v počítači.

K obrázku se také přidávat atribut alt = alternative text, který se používá pro lidi, kteří používají screen reader. Tak aby jim to řeklo, co se na obrázku nachází

A title, což je jednoduché popsání obrázku.

Správný kód vypadá takhle

<img src="odkaz na obrazek" alt="Pes co skejtuje a přitom ho honí včela" title="Pes na skejtu">

Pokud chceme obrázek umístit před text, což je graficky vážně hrozný, umístíme kód do p

Pokud ho chceme dát o řádek nad, vložíme kód před p

K obrázku se ještě váží elementy figure a figcaption. Figure je element, který z obrázku vytvoří samostanou jednotku, a to se poté dobře stylizuje zároveň je to jediný způsob jak pomocí figcaption přidat popisek. Figure se zárověň používá k citacím, poezii atp

*[chybějící obrázek: 17d678084b55bcb075e8ececd07abe96.png]*

### HTML atributy

Zatím asi nejsložitější kapitola HTML atributy

zatím ovládáme několik HTML tagů

h1

h2

h3

h4

h5

h6

p

em

strong


<> tag
<//p> elemnt v tagu

teď přidáme i tag <//a> neboli anchor = kotva. Který se používá pro vytvoření hyperodkazu, avšak jeho použítí je lehce složitější. Musíme použít tktv. atributy. Atributy se používají pokud potřebujeme dát elementu další informace v případě linků používáme href neboli zkratka pro hypertext reference.

Správné použíti href
*[chybějící obrázek: 24d4288a9bd93d5dd6f620da0554f6ce.png]*

Pokud použijeme tento atribut stránka se nám otevře v okně, ve kterém jsme. Aby se nám link otevřel v novém okně musíme použít targe="_blank" atributu
<a href="https://maps.google.com/" target="_blank">Go to Google Maps</a>



<p>Although most polar bears are born on land, they spend most of their time on the sea ice. Their scientific name means "<a href="https://en.wikipedia.org/wiki/Sea">maritime</a> bear" and derives from this fact. Polar bears hunt their preferred food of seals from the edge of <a href="https://en.wikipedia.org/wiki/Sea_ice ">sea ice</a>, often living off fat reserves when no sea ice is present. Because of their dependence on the sea ice, polar bears are classified as <a href="https://en.wikipedia.org/wiki/Marine_mammal" target="_blank">marine mammals.</a></p>

### HTML-CSS struktura webu

</header> struktura, na horní části webu, kde je většinou logo a případně nav
</nav> struktura, kde se většinou nachází menu, díky kterému se můžeme navigovat po stránce
</section> sekce s relativním kontentem
</article> obsah, například příspěvek na blogu nebo novinový článek
<f/ooter> sekce na spodní stránce obrazovky, kde jsou dodatečné linky případně socky
</aside> obsah, který je komplementární, ale není zásadní pro hlavní obsah stránky
</figure> seskupuje obrázek a popisek

Počítačové rozložení
*[chybějící obrázek: 0a8161c36a132427561aaa091b764a4a.png]*

Mobilní rozložení
*[chybějící obrázek: 43a9e37cf7e5fe0f0d0c30e4562d36e8.png]*

Block elemnty se roztáhnou po celé šířce
Headings
Paragraphs (p)
Lists and list items (ul, ol, li)
Structuring elements (header, nav, section, article, aside, figure, footer)


Inline elementy jsou takové, že pokud je šířka obrazovky dost velká, tak se umístí vedle sebe
Images (img)
Emphasized text (em)
Strong text (strong)
Links (a)
### Elements in list
jsou dva typy listů, které můžeme pomocí HTML udělat

Unordered list <ul>
Ordered list<ol>

s tím, že elemnt ul nebo ol vložíme na začátek a pak ke každé položce ještě přidáme elemnt li jako list

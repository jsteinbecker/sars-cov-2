





 (function(w, d) {
 w.config = w.config || {};
 w.config.mustardcut = false;

 
 if (w.matchMedia && w.matchMedia('only print, only all and (prefers-color-scheme: no-preference), only all and (prefers-color-scheme: light), only all and (prefers-color-scheme: dark)').matches) {
 w.config.mustardcut = true;
 d.classList.add('js');
 d.classList.remove('grade-c');
 }
 })(window, document.documentElement);
 

 (function () {
 if ( typeof window.CustomEvent === "function" ) return false;
 function CustomEvent ( event, params ) {
 params = params || { bubbles: false, cancelable: false, detail: null };
 var evt = document.createEvent( 'CustomEvent' );
 evt.initCustomEvent( event, params.bubbles, params.cancelable, params.detail );
 return evt;
 }

 CustomEvent.prototype = window.Event.prototype;

 window.CustomEvent = CustomEvent;
 })();



Pandemics: spend on surveillance, not prediction








































































(function(e){var t=e.documentElement,n=e.implementation;t.className='js';if(n&&n.hasFeature('http://www.w3.org/TR/SVG11/feature#Image','1.1')){t.className+=' svg'}})(document)


























 window.dataLayer = [{"content":{"category":{"contentType":"comment","legacy":{"webtrendsPrimaryArticleType":"comments & opinion","webtrendsSubjectTerms":"diseases;ebola-virus;epidemiology","webtrendsContentCategory":null,"webtrendsContentCollection":null,"webtrendsContentGroup":"Nature","webtrendsContentGroupType":null,"webtrendsContentSubGroup":"Comment"}},"article":{"doi":"10.1038/d41586-018-05373-w"},"attributes":{"cms":"core media","deliveryPlatform":"oscar","copyright":{"open":false,"legacy":{"webtrendsLicenceType":null}}},"contentInfo":{"authors":["Edward C. Holmes","Andrew Rambaut","Kristian G. Andersen"],"publishedAt":1528329600,"publishedAtString":"2018-06-07","title":"Pandemics: spend on surveillance, not prediction","legacy":null,"publishedAtTime":null,"documentType":"aplusplus"},"journal":{"pcode":"nature","title":"nature","volume":"558","issue":"7709"},"authorization":{"status":true},"features":[{"name":"furtherReadingSection","present":false}],"collection":null},"page":{"category":{"pageType":"article"},"attributes":{"template":"magazine mosaic","featureFlags":[{"name":"ab\_test\_news\_feature","active":false},{"name":"ab\_test\_highlight\_supp\_info","active":false},{"name":"nature-oa-paywall","active":true},{"name":"nature-onwards-journey","active":false}],"testGroup":null},"search":null},"privacy":{},"version":"1.0.0","product":null,"session":null,"user":null,"backHalfContent":false,"country":"US","hasBody":false,"uneditedManuscript":false,"twitterId":["o3xnx","o43y9","o3ef7"]}];
 window.dataLayer.push({
 ga4MeasurementId: 'G-ERRNTNZ807',
 ga360TrackingId: 'UA-71668177-1',
 twitterId: ['3xnx', 'o43y9', 'o3ef7'],
 ga4ServerUrl: 'https://collect.nature.com',
 imprint: 'nature'
 });


 window.dataLayer.push({
 cmpAndNewGtmFeatureFlag: true
 });
 


 window.initGTM = function() {
 if (window.config.mustardcut) {
 (function (w, d, s, l, i) {
 w[l] = w[l] || [];
 w[l].push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
 var f = d.getElementsByTagName(s)[0],
 j = d.createElement(s),
 dl = l != 'dataLayer' ? '&l=' + l : '';
 j.async = true;
 
 j.src = 'https://collect.nature.com/gtm.js?id=' + i + dl;
 
 f.parentNode.insertBefore(j, f);
 })(window, document, 'script', 'dataLayer', 'GTM-MRVXSHQ');
 }
 }



 (function(w,d,t) {
 function cc() {
 var h = w.location.hostname;
 if (h.indexOf('preview-www.nature.com') > -1) return;

 var e = d.createElement(t),
 s = d.getElementsByTagName(t)[0];

 if (h.indexOf('nature.com') > -1) {
 e.src = 'https://push-content.springernature.io/pcf\_sb\_5\_1617714720898560639/production\_live/consent-bundle-8-8.js';
 e.setAttribute('onload', "initGTM(window,document,'script','dataLayer','GTM-MRVXSHQ')");
 } else {
 e.src = '/static/js/cookie-consent-es5-bundle-444fb65518.js';
 e.setAttribute('data-consent', h);
 }
 s.insertAdjacentElement('afterend', e);
 }

 cc();
 })(window,document,'script');


 window.eligibleForRa21 = 'true'; // required by js files for displaying the cobranding box (entitlement-box.js)
 window.idpVerifyPrefix = 'https://verify.nature.com';
 window.ra21Host = 'https://wayf.springernature.com';
 

 (function(w, d) {
 w.idpVerifyPrefix = 'https://verify.nature.com';
 w.ra21Host = 'https://wayf.springernature.com';
 var moduleSupport = (function() {
 return 'noModule' in d.createElement('script');
 })();

 var polyfillsUrl = function() {
 var features = {
 'IntersectionObserver': window.IntersectionObserver,
 'Promise': window.Promise,
 'URLSearchParams': window.URLSearchParams,
 'Symbol.iterator': window.Symbol && Symbol.iterator,
 'Array.from': Array.from,
 'Array.prototype.includes': Array.prototype.includes,
 'Array.prototype.find': Array.prototype.find,
 'Array.prototype.forEach': Array.prototype.forEach,
 'NodeList.prototype.forEach': NodeList.prototype.forEach,
 'Element.prototype.closest': Element.prototype.closest,
 'Element.prototype.prepend': Element.prototype.prepend,
 'Element.prototype.remove': Element.prototype.remove,
 'Object.assign': Object.assign
 };
 var req = [];
 for (var feature in features) {
 if (Object.prototype.hasOwnProperty.call(features, feature) && !features[feature]) {
 req.push(feature);
 }
 }
 if (req.length) {
 return 'https://polyfill.io/v3/polyfill.min.js?features=' + req.join('%2C') + '&flags=always';
 }
 return null;
 };

 if (w.config.mustardcut === true) {
 w.loader = {
 index: 0,
 registered: [],
 scripts: [
 {src: polyfillsUrl(), test: 'polyfills-js', noinit: true},
 
 {src: '/static/js/magazine/magazine-mosaic-fa774b60d8.js', test: 'magazine-mosaic-js'},
 {src: '/static/js/shared-es6-bundle-52043d4c0f.js', test: 'shared-js', module: true},
 {src: '/static/js/shared-es5-bundle-19fd0d3511.js', test: 'shared-js', nomodule: true},
 {src: '/static/js/header-150-es6-bundle-5bb959eaa1.js', test: 'header-150-js', module: true},
 {src: '/static/js/header-150-es5-bundle-88bc691ce2.js', test: 'header-150-js', nomodule: true}
 
 ].filter(function (s) {
 if (s.src === null) return false;
 if (moduleSupport && s.nomodule) return false;
 return !(!moduleSupport && s.module);
 }),

 register: function (value) {
 this.registered.push(value);
 },

 ready: function () {
 if (this.registered.length === this.scripts.length) {
 this.registered.forEach(function (fn) {
 if (typeof fn === 'function') {
 setTimeout(fn, 0); 
 }
 });
 this.ready = function () {};
 }
 },

 insert: function (s) {
 var t = d.getElementById('js-position' + this.index);
 if (t && t.insertAdjacentElement) {
 t.insertAdjacentElement('afterend', s);
 } else {
 d.head.appendChild(s);
 }
 ++this.index;
 },

 createScript: function (script, beforeLoad) {
 var s = d.createElement('script');
 s.id = 'js-position' + (this.index + 1);
 s.setAttribute('data-test', script.test);
 if (beforeLoad) {
 s.defer = 'defer';
 s.onload = function () {
 if (script.noinit) {
 loader.register(true);
 }
 if (d.readyState === 'interactive' || d.readyState === 'complete') {
 loader.ready();
 }
 };
 } else {
 s.async = 'async';
 }
 s.src = script.src;
 return s;
 },

 init: function () {
 this.scripts.forEach(function (s) {
 loader.insert(loader.createScript(s, true));
 });

 d.addEventListener('DOMContentLoaded', function () {
 loader.ready();
 
 var conditionalScripts = null;
 

 if (conditionalScripts) {
 conditionalScripts.filter(function (script) {
 return !!document.querySelector(script.match) && !((moduleSupport && script.nomodule) || (!moduleSupport && script.module));
 }).forEach(function (script) {
 loader.insert(loader.createScript(script));
 });
 }
 }, false);
 }
 };
 loader.init();
 }
 })(window, document);
 



[Skip to main content](#content)


Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain
 the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in
 Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles
 and JavaScript.







Advertisement




[![Advertisement](//pubads.g.doubleclick.net/gampad/ad?iu=/285/nature.com/article&sz=728x90&c=-1386506511&t=pos%3Dtop%26type%3Darticle%26artid%3Dd41586-018-05373-w%26doi%3D10.1038/d41586-018-05373-w%26subjmeta%3D174,2042,326,478,596,631,692,699,700%26kwrd%3DDiseases,Ebola+virus,Epidemiology)](//pubads.g.doubleclick.net/gampad/jump?iu=/285/nature.com/article&sz=728x90&c=-1386506511&t=pos%3Dtop%26type%3Darticle%26artid%3Dd41586-018-05373-w%26doi%3D10.1038/d41586-018-05373-w%26subjmeta%3D174,2042,326,478,596,631,692,699,700%26kwrd%3DDiseases,Ebola+virus,Epidemiology)









[![Nature](//media.springernature.com/full/nature-cms/uploads/product/nature/header-86f1267ea01eccd46b530284be10585e.svg)](/)

* [View all journals](https://www.nature.com/siteindex)
* [Search](#search-menu)
* [My Account](/nams/svc/myaccount)
[Login](https://idp.nature.com/authorize/natureuser?client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fd41586-018-05373-w)









* [Explore content](#explore)
* [About the journal](#about-the-journal)
* [Publish with us](#publish-with-us)




[Subscribe](https://www.nature.com/nature/subscribe)



* [Sign up for alerts](https://www.nature.com/my-account/alerts/subscribe-journal?list-id=1)
* [RSS feed](http://feeds.nature.com/nature/rss/current)








1. [nature](/)
2. [comment](/nature/articles?type=comment)
3. article













* COMMENT
* 07 June 2018


Pandemics: spend on surveillance, not prediction
================================================




 Trust is undermined when scientists make overblown promises about disease prevention, warn Edward C. Holmes, Andrew Rambaut and Kristian G. Andersen.
 



* [Edward C. Holmes](#author-0)
[0](#Aff0)
 ,
* [Andrew Rambaut](#author-1)
[1](#Aff1)
 &
* [Kristian G. Andersen](#author-2)
[2](#Aff2)



1. [Edward C. Holmes](mailto:edward.holmes@sydney.edu.au)
	1. Edward C. Holmes is professor of biology at the University of Sydney, Australia.

[View author publications](/search?author="Edward C. Holmes")

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=%22Edward+C.%2BHolmes%22)
 [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&btnG=Search+Scholar&as_sauthors=%22Edward+C.%2BHolmes%22)
2. [Andrew Rambaut](mailto:a.rambaut@ed.ac.uk)
	1. Andrew Rambaut is professor of molecular evolution at the University of Edinburgh, UK.

[View author publications](/search?author="Andrew Rambaut")

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=%22Andrew%2BRambaut%22)
 [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&btnG=Search+Scholar&as_sauthors=%22Andrew%2BRambaut%22)
3. [Kristian G. Andersen](mailto:andersen@scripps.edu)
	1. Kristian G. Andersen is assistant professor of immunology and microbiology at The Scripps Research Institute, La Jolla, California, USA.

[View author publications](/search?author="Kristian G. Andersen")

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=%22Kristian+G.%2BAndersen%22)
 [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&btnG=Search+Scholar&as_sauthors=%22Kristian+G.%2BAndersen%22)





* [Twitter](https://twitter.com/intent/tweet?text=Pandemics%3A+spend+on+surveillance%2C+not+prediction&url=https%3A%2F%2Fwww.nature.com%2Farticles%2Fd41586-018-05373-w)
* [Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.nature.com%2Farticles%2Fd41586-018-05373-w)
* [Email](mailto:?subject=Pandemics: spend on surveillance, not prediction&body=https%3A%2F%2Fwww.nature.com%2Farticles%2Fd41586-018-05373-w)







You have full access to this article via your institution.



[Download PDF](/articles/d41586-018-05373-w.pdf)






[Download PDF](//media.nature.com/original/magazine-assets/d41586-018-05373-w/d41586-018-05373-w.pdf)





![A health official uses a thermometer to measure the temperature of passengers disembarking a plane in DRC, May 2018]()

![A health official uses a thermometer to measure the temperature of passengers disembarking a plane in DRC, May 2018](//media.nature.com/lw800/magazine-assets/d41586-018-05373-w/d41586-018-05373-w_15811348.jpg)


A health official checks for Ebola symptoms by taking the temperature of passengers arriving at Mbandaka Airport in the Democratic Republic of the Congo.Credit: Junior Kannah/AFP/Getty




The resurgence of Ebola virus in the Democratic Republic of the Congo this May is a stark reminder that no amount of DNA sequencing can tell us when or where the next virus outbreak will appear. More genome sequence data were obtained for the 2013–16 Ebola epidemic than for any other single disease outbreak. Still, health workers in Mbandaka, the country’s northwestern provincial capital, are [scrambling to contain a growing number of cases](https://www.nature.com/articles/d41586-018-05205-x).

Over the past 15 years or so, outbreaks caused by viruses such as Ebola, SARS and Zika have cost governments billions of US dollars. Combined with a perception among scientists, health workers and citizens that responses to outbreaks have been inadequate, [this has fuelled what seems like a compelling idea](https://www.nature.com/news/data-sharing-make-outbreak-research-open-access-1.16966). Namely, that if researchers can identify the next pandemic virus before the first case appears, communities could drastically improve strategies for control, and even stop a virus from taking hold[1](#ref-CR1),[2](#ref-CR2). Indeed, since 2009, the US Agency for International Development has spent US$170 million on evaluating the “feasibility of preemptively mitigating pandemic threats”[1](#ref-CR1).

Various experts have flagged up problems with this approach (including the three of us)[3](#ref-CR3),[4](#ref-CR4). Nonetheless, an ambitious biodiversity-based approach to outbreak prediction — the [Global Virome Project](http://www.globalviromeproject.org) — was announced in February this year, with its proponents soliciting $1.2 billion in funding from around the world (see ‘High stakes’). They estimate that other mammals and birds contain 1.67 million unknown viruses from the families of viruses that are most likely to jump to humans, and will use the funding to conduct a genomic survey of these unknown viruses, with the aim of predicting which might infect people[1](#ref-CR1).



![]()

![](//media.nature.com/lw800/magazine-assets/d41586-018-05373-w/d41586-018-05373-w_15827012.jpg)


Sources: NIH; Global Virome Project




Broad genomic surveys of animal viruses will almost certainly advance our understanding of virus diversity and evolution. In our view, they will be of little practical value when it comes to understanding and mitigating the emergence of disease.

We urge those working on infectious disease to focus funds and efforts on a much simpler and more cost-effective way to mitigate outbreaks — proactive, real-time surveillance of human populations.

The public has increasingly questioned the scientific credibility of researchers working on outbreaks. In the 2013–16 Ebola epidemic, for instance, the international response was repeatedly [criticized for being too slow](https://www.nature.com/news/disease-outbreak-finish-the-fight-against-ebola-1.18109). And during the 2009 H1N1 influenza epidemic, people asked whether the severity of the virus had been overblown, and if the stockpiling of pharmaceuticals was even necessary[5](#ref-CR5). Making promises about disease prevention and control that cannot be kept will only further undermine trust.

**Forecasting fallacy**

Supporters of outbreak prediction maintain that if biologists genetically characterize all of the viruses circulating in animal populations (especially in groups such as bats and rodents that have previously acted as reservoirs for emerging viruses), they can determine which ones are likely to emerge next, and ultimately prevent them from doing so. With enough data, coupled with artificial intelligence and machine learning, they argue, the process could be similar to predicting the weather[6](#ref-CR6).



![A Congolese child washes her hands as a preventive measure against Ebola in DRC, May 2018]()

![A Congolese child washes her hands as a preventive measure against Ebola in DRC, May 2018](//media.nature.com/lw800/magazine-assets/d41586-018-05373-w/d41586-018-05373-w_15811350.jpg)


People in Mbandaka are taking extra precautionary measures to stop the spread of Ebola virus.Credit: Kenny Katombe/Reuters




Reams of data are available to train models to predict the weather. By contrast, it is exceedingly rare for viruses to emerge and cause outbreaks. Around 250 human viruses have been described, and only a small subset of these have caused major epidemics this century.

Advocates of prediction also argue that it will be possible to anticipate how likely a virus is to emerge in people on the basis of its sequence, and by using knowledge of how it interacts with cells (obtained, for instance, by studying the virus in human cell cultures).

This is misguided. Determining which of more than 1.6 million animal viruses are capable of replicating in humans and transmitting between them would require many decades’ worth of laboratory work in cell cultures and animals. Even if researchers managed to link each virus genome sequence to substantial experimental data, all sorts of other factors determine whether a virus jumps species and emerges in a human population, such as the distribution and density of animal hosts. Influenza viruses have circulated in horses since the 1950s and in dogs since the early 2000s, for instance[7](#ref-CR7). These viruses have not emerged in human populations, and perhaps never will — for unknown reasons.

In short, there aren’t enough data on virus outbreaks for researchers to be able to accurately predict the next outbreak strain. Nor is there a good enough understanding of what drives viruses to jump hosts, making it difficult to construct predictive models.

Biodiversity-based prediction also ignores the fact that viruses are not fixed entities. New variants of RNA viruses appear every day. This speedy evolution means that surveys would need to be done continuously to be informative. The cost would dwarf the proposed $1.2-billion budget for one-time sequencing.

Even if it were possible to identify which viruses are likely to emerge in humans, thousands of candidates could end up being identified, each with a low probability of causing an outbreak. What should be done in that case? Costs would skyrocket if vaccines and therapeutics were proposed for even a handful of these.

**Screen and sequence**

Currently, the most effective and realistic way to fight outbreaks is to monitor human populations in the countries and locations that are most vulnerable to infectious disease. This can be done by local clinicians, health workers in non-governmental organizations such as Médecins Sans Frontières (MSF; also known as Doctors Without Borders), and global institutions such as the World Health Organization (WHO).

We advocate the detailed screening of people who are exhibiting symptoms that cannot easily be diagnosed. Such tests should use the latest sequencing technologies to characterize all the pathogens that have infected an individual — the human ‘infectome’[8](#ref-CR8). To track previous infections, investigators should also assess each person’s immune response, by analysing components of their blood using broad-scale serology[9](#ref-CR9).

Emerging diseases are commonly associated with population expansions — when people encroach on habitats occupied by animals — as well as with environmental disturbances and climate change. Deforestation, for instance, can promote human interactions with animals that carry new threats, and can increase encounters with new vector species such as ticks and mosquitoes[10](#ref-CR10). Animal die-offs, for example that of bar-headed geese (*Anser indicus*) at Lake Qinghai in China in 2005 (which was caused by the H5N1 influenza virus), can also flag problem regions or emerging pathogens. Surveillance efforts should therefore focus on communities that live and work in such environments.

Identifying which pathogen is causing an outbreak is no longer the bottleneck it once was. It took researchers two years to determine HIV as the cause of AIDS in the early 1980s using microscopy and other techniques. By contrast, in 2012 it took only weeks for investigators using genomic technologies to discover the coronavirus that caused Middle East respiratory syndrome (MERS).

Rapid identification of viruses can be achieved only if such technologies — and the people trained to use them — are globally available, including in resource-limited regions where the risk of outbreaks might be higher. Thankfully, relevant capacity-building programmes are now beginning to be established, such as the Human Heredity and Health in Africa (H3Africa) Initiative, run by the UK Wellcome Trust and the US National Institutes of Health[11](#ref-CR11).

Once an emerging outbreak virus has been identified, it needs to be analysed quickly to establish what type it is; which molecular mechanisms (such as receptor type) enable it to jump between individuals; how it spreads through human populations; and how it affects those infected. In other words, at least four kinds of analysis are needed: genomic, virological, epidemiological and clinical. And the data must be passed to key stakeholders, from researchers and health workers on the ground to international agencies such as the WHO and the MSF. Data must be kept as free of restrictions as possible, within the constraints of protections of patient privacy and other ethical issues.

This will best be achieved through an established global network of highly trained local researchers, such as the WHO Global Outbreak Alert and Response Network (GOARN). Real-time tools for reconstructing and tracking outbreaks at the genomic level, such as portable sequencing devices, are improving fast[8](#ref-CR8). Information gathered during recent outbreaks has quickly had tangible impacts on public-health decisions, largely owing to data generation and analysis by many research teams within days of people being infected[12](#ref-CR12).

For instance, in the 2013–16 Ebola epidemic, genome sequencing of the virus proved that a person could sexually transmit the disease more than a year after becoming infected. This prompted the WHO to increase its recommended number of tests for persistent infection in survivors of the disease.

Ultimately, the challenge is to link genomic, clinical and epidemiological data within days of an outbreak being detected, including information about how people in an affected community are interacting. Such an open, collaborative approach to tackling the emergence of infectious disease is now possible. This is partly thanks to technology, but is mainly due to a shift in perception about the importance of this approach. At least in genomic epidemiology, there is a growing move towards real-time, open-access data and analysis, aided by the use of preprint servers and wikis such as Virological (<http://virological.org>). This type of collaborative effort can complement the work of agencies including the WHO and the MSF, which focus predominantly on providing information, isolating those who have been infected, and so on.

So far, researchers have sampled little of the viral universe. Surveys of animals will undoubtedly result in the discovery of many thousands of new viruses. These data will benefit studies of diversity and evolution, and could tell us whether and why some pathogens might jump species boundaries more frequently than others. But, given the rarity of outbreaks and the complexity of host–pathogen interactions, it is arrogant to imagine that we could use such surveys to predict and mitigate the emergence of disease.

New viruses will continue to emerge unexpectedly. There is a lot we can and must do to be better prepared.



*Nature* **558**, 180-182 (2018)


*doi: https://doi.org/10.1038/d41586-018-05373-w*



References
----------

1. Carroll, D. *et al.* *Science* **359**, 872–874 (2018).

[Article](https://doi.org/10.1126%2Fscience.aap7463) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Science&volume=359&pages=872-874&publication_year=2018&author=Carroll%2CD.)
2. Carroll, D. *et al.* *Bull. World Health Organ.* **96**, 292–294 (2018).

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=29695886) 
 [Article](https://doi.org/10.2471%2FBLT.17.205005) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Bull.%20World%20Health%20Organ.&volume=96&pages=292-294&publication_year=2018&author=Carroll%2CD.)
3. Garrett, L. *Lancet* **391**, 827–828 (2018).

[Article](https://doi.org/10.1016%2FS0140-6736%2818%2930433-1) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Lancet&volume=391&pages=827-828&publication_year=2018&author=Garrett%2CL)
4. Yong, E. ‘[Is it possible to predict the next pandemic?](https://www.theatlantic.com/science/archive/2017/10/pandemic-prediction-challenge/543954/)’ *The Atlantic* (25 October 2017).
5. Godlee, F. *Br. Med. J.* **340**, c2947 (2010).

[Article](https://doi.org/10.1136%2Fbmj.c2947) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Br.%20Med.%20J.&volume=340&publication_year=2010&author=Godlee%2CF.)
6. Morrison, J. ‘[Can virus hunters stop the next pandemic before it happens?](https://www.smithsonianmag.com/science-nature/how-to-stop-next-animal-borne-pandemic-180967908/)’ Smithsonian (25 January 2018).
7. Parrish, C. R., Murcia, P. R. & Holmes, E. C. *J. Virol.* **89**, 2990–2994 (2015).

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25540375) 
 [Article](https://doi.org/10.1128%2FJVI.03146-14) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=J.%20Virol.&volume=89&pages=2990-2994&publication_year=2015&author=Parrish%2CC.%20R.&author=Murcia%2CP.%20R.&author=Holmes%2CE.%20C.)
8. Gardy, J. L. & Loman, N. J. *Nature Rev. Genet.* **19**, 9–20 (2018).

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=29129921) 
 [Article](https://doi.org/10.1038%2Fnrg.2017.88) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Nature%20Rev.%20Genet.&volume=19&pages=9-20&publication_year=2018&author=Gardy%2CJ.%20L.&author=Loman%2CN.%20J.)
9. Xu, G. J. *et al.* *Science* **348**, aaa0698 (2015).

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=26045439) 
 [Article](https://doi.org/10.1126%2Fscience.aaa0698) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Science&volume=348&publication_year=2015&author=Xu%2CG.%20J.)
10. Keesing, F. *et al.* *Nature* **468**, 647–652 (2010).

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=21124449) 
 [Article](https://doi.org/10.1038%2Fnature09575) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Nature&volume=468&pages=647-652&publication_year=2010&author=Keesing%2CF.)
11. H3Africa Consortium. *Science* **344**, 1346–1348 (2014).

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=24948725) 
 [Article](https://doi.org/10.1126%2Fscience.1251546) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Science&volume=344&pages=1346-1348&publication_year=2014&author=null%2CH3Africa%20Consortium)
12. Gire, S. K. *et al.* *Science* **345**, 1369–1372 (2014).

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25214632) 
 [Article](https://doi.org/10.1126%2Fscience.1259657) 
 [Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Science&volume=345&pages=1369-1372&publication_year=2014&author=Gire%2CS.%20K.)

[Download references](https://citation-needed.springer.com/v2/references/10.1038/d41586-018-05373-w?format=refman&flavour=references)



Related Articles
----------------


* ### 
[Experimental drugs poised for use in Ebola outbreak](https://www.nature.com/articles/d41586-018-05205-x)
* ### 
[Data sharing: Make outbreak research open access](https://www.nature.com/news/data-sharing-make-outbreak-research-open-access-1.16966)
* ### 
[Disease outbreak: Finish the fight against Ebola](https://www.nature.com/news/disease-outbreak-finish-the-fight-against-ebola-1.18109)
* ### 
[Ebola outbreak in Africa ends — but gaps in public health leave region vulnerable](https://www.nature.com/news/ebola-outbreak-in-africa-ends-but-gaps-in-public-health-leave-region-vulnerable-1.22227)


Subjects
--------


* [Diseases](/subjects/diseases)
* [Ebola virus](/subjects/ebola-virus)
* [Epidemiology](/subjects/epidemiology)




Latest on:
----------




Diseases



[![African leadership underpins success of malaria drug trial](https://images.nature.com/w140h79/magazine-assets/d41586-022-00573-x/d41586-022-00573-x_20192694.jpg)
### African leadership underpins success of malaria drug trial


Nature Index 09 MAR 22](http://www.nature.com/articles/d41586-022-00573-x)


[![Could drugs prevent Alzheimer’s? These trials aim to find out](https://images.nature.com/w140h79/magazine-assets/d41586-022-00651-0/d41586-022-00651-0_20188694.jpg)
### Could drugs prevent Alzheimer’s? These trials aim to find out


News Feature 09 MAR 22](http://www.nature.com/articles/d41586-022-00651-0)


[![Regulation of liver subcellular architecture controls metabolic homeostasis](https://media.nature.com/w140h79/springer-static/image/art%3A10.1038%2Fs41586-022-04488-5/MediaObjects/41586_2022_4488_Fig1_HTML.png)
### Regulation of liver subcellular architecture controls metabolic homeostasis


Article 09 MAR 22](http://www.nature.com/articles/s41586-022-04488-5)





Ebola virus



[![Resurgence of Ebola virus in 2021 in Guinea suggests a new paradigm for outbreaks](https://media.nature.com/w140h79/springer-static/image/art%3A10.1038%2Fs41586-021-03901-9/MediaObjects/41586_2021_3901_Fig1_HTML.png)
### Resurgence of Ebola virus in 2021 in Guinea suggests a new paradigm for outbreaks


Article 15 SEP 21](http://www.nature.com/articles/s41586-021-03901-9)


[![Antibodies periodically wax and wane in survivors of Ebola](https://images.nature.com/w140h79/magazine-assets/d41586-020-03044-3/d41586-020-03044-3_18538576.png)
### Antibodies periodically wax and wane in survivors of Ebola


News & Views 27 JAN 21](http://www.nature.com/articles/d41586-020-03044-3)


[![Why did the world’s pandemic warning system fail when COVID hit?](https://images.nature.com/w140h79/magazine-assets/d41586-021-00162-4/d41586-021-00162-4_18782590.jpg)
### Why did the world’s pandemic warning system fail when COVID hit?


News 23 JAN 21](http://www.nature.com/articles/d41586-021-00162-4)





Epidemiology



[![Had Omicron? You're unlikely to catch its rising variant](https://images.nature.com/w140h79/magazine-assets/d41586-022-00558-w/d41586-022-00558-w_20169024.jpg)
### Had Omicron? You're unlikely to catch its rising variant


News 25 FEB 22](http://www.nature.com/articles/d41586-022-00558-w)


[![Fourth dose of COVID vaccine offers only slight boost against Omicron infection](https://images.nature.com/w140h79/magazine-assets/d41586-022-00486-9/d41586-022-00486-9_20151098.jpg)
### Fourth dose of COVID vaccine offers only slight boost against Omicron infection


News 23 FEB 22](http://www.nature.com/articles/d41586-022-00486-9)


[![Commit to transparent COVID data until the WHO declares the pandemic is over](https://images.nature.com/w140h79/magazine-assets/d41586-022-00424-9/d41586-022-00424-9_20083424.jpg)
### Commit to transparent COVID data until the WHO declares the pandemic is over


World View 22 FEB 22](http://www.nature.com/articles/d41586-022-00424-9)











Nature Careers
---------------



### 
[Jobs](https://www.nature.com/naturecareers/)



* #### 
[Principal Investigator / Faculty](https://www.nature.com/naturecareers/job/principal-investigator-faculty-san-diego-biomedical-research-institute-sdbri-755398)



San Diego Biomedical Research Institute (SDBRI)


Multiple locations
* #### 
[Research Associate / Light Microscopy Imaging Specialist (m/f/x)](https://www.nature.com/naturecareers/job/research-associate-light-microscopy-imaging-specialist-mfx-technische-universitat-dresden-tu-dresden-755396)



Technische Universität Dresden (TU Dresden)


01069 Dresden, Germany
* #### 
[Bioinformatician (m/f/div)](https://www.nature.com/naturecareers/job/bioinformatician-mfdiv-max-planck-institute-for-plant-breeding-research-mpipz-755395)



Max Planck Institute for Plant Breeding Research (MPIPZ)


Cologne, Germany
* #### 
[Research Coordinator / Institute Manager (div/f/m)](https://www.nature.com/naturecareers/job/research-coordinator-institute-manager-divfm-max-planck-institute-for-astrophysics-mpa-755394)



Max Planck Institute for Astrophysics (MPA)


Garching near Munich, Germany









You have full access to this article via your institution.



[Download PDF](/articles/d41586-018-05373-w.pdf)






[Download PDF](//media.nature.com/original/magazine-assets/d41586-018-05373-w/d41586-018-05373-w.pdf)


Related Articles
----------------


* ### 
[Experimental drugs poised for use in Ebola outbreak](https://www.nature.com/articles/d41586-018-05205-x)
* ### 
[Data sharing: Make outbreak research open access](https://www.nature.com/news/data-sharing-make-outbreak-research-open-access-1.16966)
* ### 
[Disease outbreak: Finish the fight against Ebola](https://www.nature.com/news/disease-outbreak-finish-the-fight-against-ebola-1.18109)
* ### 
[Ebola outbreak in Africa ends — but gaps in public health leave region vulnerable](https://www.nature.com/news/ebola-outbreak-in-africa-ends-but-gaps-in-public-health-leave-region-vulnerable-1.22227)


Subjects
--------


* [Diseases](/subjects/diseases)
* [Ebola virus](/subjects/ebola-virus)
* [Epidemiology](/subjects/epidemiology)




[![Advertisement](//pubads.g.doubleclick.net/gampad/ad?iu=/285/nature.com/article&sz=300x250&c=-150342402&t=pos%3Dright%26artid%3D/articles/d41586-018-05373-w)](//pubads.g.doubleclick.net/gampad/jump?iu=/285/nature.com/article&sz=300x250&c=-150342402&t=pos%3Dright%26artid%3D/articles/d41586-018-05373-w)





Sign up to Nature Briefing
--------------------------


An essential round-up of science news, opinion and analysis, delivered to your inbox every weekday.






Email address



Yes! Sign me up to receive the daily *Nature Briefing* email. I agree my information will be processed in accordance with the *Nature* and Springer Nature Limited [Privacy Policy](https://www.nature.com/info/privacy).

Sign up










![](/platform/track/article/d41586-018-05373-w)





xml version="1.0" encoding="UTF-8" standalone="no"?

Close banner






Close





![Nature Briefing](/static/images/logos/nature-briefing-logo-n150-white.svg)
Sign up for the *Nature Briefing* newsletter — what matters in science, free to your inbox daily.







Email address


Sign up



I agree my information will be processed in accordance with the *Nature* and Springer Nature Limited [Privacy Policy](https://www.nature.com/info/privacy).









xml version="1.0" encoding="UTF-8" standalone="no"?

Close banner






Close



Get the most important science stories of the day, free in your inbox.
[Sign up for Nature Briefing](/briefing/signup/?origin=Nature&originReferralPoint=EmailBanner) 






 if (window.config.mustardcut) {
 window.onload = function () {
 Array.prototype.slice.call(document.querySelectorAll(".magazine-infographic > iframe"))
 .forEach(function (element) {
 function listener(event) {
 if (event.data.height) {
 if (element.id === event.data.requestData.id) {
 element.setAttribute("height", event.data.height)
 }
 }
 }

 window.addEventListener("message", listener);
 element.contentWindow.postMessage({name: "getHeight", id: element.id}, "*");
 });
 }
 }
 

 var idp = {
 hasNatureUserProof: function (hasProof) {
 if (!hasProof) {
 document.getElementById("my-account").setAttribute("style", "display: none;");
 document.getElementById("login-button").setAttribute("style", "");
 }
 }
 }
 


Explore content
---------------


* [Research articles](/nature/research-articles)
* [News](/news)
* [Opinion](/opinion)
* [Research Analysis](/research-analysis)
* [Careers](/careers)
* [Books & Culture](/books-culture)
* [Podcasts](/nature/podcasts)
* [Videos](/nature/videos)
* [Current issue](/nature/current-issue)
* [Browse issues](/nature/browse-issues)
* [Collections](/nature/collections)
* [Subjects](/nature/browse-subjects)
* [Follow us on Facebook](https://www.facebook.com/Nature)
* [Follow us on Twitter](https://twitter.com/nature)
* [Subscribe](https://www.nature.com/nature/subscribe)
* [Sign up for alerts](https://www.nature.com/my-account/alerts/subscribe-journal?list-id=1)
* [RSS feed](http://feeds.nature.com/nature/rss/current)






About the journal
-----------------


* [Journal Staff](/nature/journal-staff)
* [About the Editors](/nature/editors)
* [Journal Information](/nature/journal-information)
* [Our publishing models](/nature/our-publishing-models)
* [Editorial Values Statement](/nature/editorial-values-statement)
* [Journal Impact](/nature/journal-impact)
* [Awards](/nature/awards)
* [Contact](/nature/contact)
* [Editorial policies](/nature/editorial-policies)
* [History of Nature](/nature/history-of-nature)
* [Send a news tip](/nature/send-a-news-tip)






Publish with us
---------------


* [For Authors](/nature/for-authors)
* [For Referees](/nature/for-referees)
* [Submit manuscript](https://mts-nature.nature.com/)






Search
------





Search articles by subject, keyword or author





Show results from

All journals



Search







[Advanced search](/search/advanced) 




### Quick links


* [Explore articles by subject](/subjects)
* [Find a job](/naturecareers)
* [Guide to authors](/authors/index.html)
* [Editorial policies](/authors/editorial_policies/)











 Nature (*Nature*)
 

ISSN 1476-4687 (online)
 

ISSN 0028-0836 (print)
 










nature.com sitemap
------------------




![Nature portfolio](/static/images/logos/nature-portfolio-white.svg)

* [About us](https://www.nature.com/npg_/company_info/index.html)
* [Press releases](https://www.nature.com/npg_/press_room/press_releases.html)
* [Press office](https://press.nature.com/)
* [Contact us](https://support.nature.com/support/home)


* 
* 
* 





### Discover content


* [Journals A-Z](https://www.nature.com/siteindex)
* [Articles by subject](https://www.nature.com/subjects/)
* [Nano](https://nano.nature.com/)
* [Protocol Exchange](https://www.nature.com/protocolexchange/)
* [Nature Index](https://www.natureindex.com/)




### Publishing policies


* [Nature portfolio policies](https://www.nature.com/authors/editorial_policies/)
* [Open access](https://www.nature.com/nature-research/open-access)




### Author & Researcher services


* [Reprints & permissions](https://www.nature.com/reprints/)
* [Research data](https://www.springernature.com/gp/authors/research-data)
* [Language editing](https://authorservices.springernature.com/go/nr)
* [Scientific editing](https://authorservices.springernature.com/scientific-editing/)
* [Nature Masterclasses](https://masterclasses.nature.com/)
* [Nature Research Academies](https://partnerships.nature.com/product/researcher-training/)




### Libraries & institutions


* [Librarian service & tools](https://www.springernature.com/gp/librarians/tools-services)
* [Librarian portal](https://www.springernature.com/gp/librarians/manage-your-account/librarianportal)
* [Open research](https://www.nature.com/openresearch/about-open-access/information-for-institutions/)
* [Recommend to library](https://www.springernature.com/gp/librarians/recommend-to-your-library)




### Advertising & partnerships


* [Advertising](https://partnerships.nature.com/product/digital-advertising/)
* [Partnerships & Services](https://partnerships.nature.com/)
* [Media kits](https://partnerships.nature.com/media-kits/)
* [Branded content](https://partnerships.nature.com/product/branded-content-native-advertising/)




### Career development


* [Nature Careers](https://www.nature.com/naturecareers)
* [Nature  Conferences](https://conferences.nature.com)
* [Nature  events](https://www.nature.com/natureevents/)




### Regional websites


* [Nature Africa](https://www.nature.com/natafrica)
* [Nature China](http://www.naturechina.com)
* [Nature India](https://www.nature.com/nindia)
* [Nature Italy](https://www.nature.com/natitaly)
* [Nature Japan](https://www.natureasia.com/ja-jp/)
* [Nature Korea](https://www.natureasia.com/ko-kr/)
* [Nature Middle East](https://www.nature.com/nmiddleeast/)




### Legal & Privacy


* [Privacy Policy](https://www.nature.com/info/privacy)
* [Use of cookies](https://www.nature.com/info/cookies)
* [Manage cookies/Do not sell my data](javascript:;)
* [Legal notice](https://www.nature.com/info/legal-notice)
* [Accessibility statement](https://www.nature.com/info/accessibility-statement)
* [Terms & Conditions](https://www.nature.com/info/terms-and-conditions)
* [California Privacy Statement](https://www.springernature.com/ccpa)










![Springer Nature](/static/images/logos/sn-logo-white.svg)

















































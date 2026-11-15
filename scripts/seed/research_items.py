# Verified research items for the May–Nov 2026 backfill.
# Every entry was opened and checked (title, publisher, date, summary) on 2026-11-15.
# Fields: url, title, publisher, author, date (YYYY-MM-DD or YYYY-MM or ""), region, kind, topics, summary, background
# background=True -> context item outside the scan window (bibliography only, not in a weekly roundup).
I = []
def add(url, title, publisher, date, region, kind, topics, summary, author="", background=False):
    I.append(dict(url=url, title=title, publisher=publisher, author=author, date=date, region=region,
                  kind=kind, topics=topics, summary=summary, background=background))

# ---------- Canada: national strategy & funding ----------
add("https://www.torys.com/en/our-latest-thinking/publications/2026/05/canada-launches-ai-scip",
    "Canada launches Artificial Intelligence Sovereign Compute Infrastructure Program: funding, eligibility, and key requirements",
    "Torys LLP", "2026-05-13", "Canada", "analysis", ["funding","research","policy"],
    "Explains the federal AI Sovereign Compute Infrastructure Program (launched April 15, 2026): up to $890M over seven years. For-profits cannot apply directly; eligible applicants are not-for-profits, post-secondary institutions and consortia.",
    author="Ramsey, J., Evans, H., Slavens, S., Thomson, I. T. D., & Wang, L.")
add("https://cifar.ca/cifarnews/2026/05/21/government-of-canada-and-cifar-announce-24m-investment-in-top-ai-talent/",
    "Government of Canada and CIFAR announce $24M investment in top AI talent", "CIFAR", "2026-05-21", "Canada", "announcement",
    ["funding","research","post-secondary"],
    "42 appointments and renewals of Canada CIFAR AI Chairs backed by $24M. The program now supports 143 Chairs, all affiliated with Amii, Mila or Vector.", author="Davidson, K.")
add("https://www.ualberta.ca/en/news/news-releases-and-statements/news-releases/2026/05-may/u-of-a-amii-announce-successful-30m-recruitment-campaign-of-top-ai-minds.html",
    "U of A, Amii announce successful $30M recruitment campaign of top AI minds", "University of Alberta", "2026-05-21", "Canada", "announcement",
    ["research","post-secondary","funding"],
    "25 researchers appointed through a $30M Amii investment supported by CIFAR, spanning AI in health, energy, space and agriculture.")
add("https://www.michaelgeist.ca/2026/06/ai-for-all-details-to-follow-government-releases-a-big-spending-ai-strategy-that-is-still-short-on-the-specifics-that-matter/",
    "AI for All, details to follow: Government releases a big-spending AI strategy that is still short on the specifics that matter",
    "Michael Geist", "2026-06-04", "Canada", "analysis", ["policy","funding","creative","safety"],
    "Critique of the federal AI for All strategy: many spending programs (including a $50M Creative Technology Program) but no AI-specific regulation, relying instead on privacy reform and online-safety legislation.", author="Geist, M.")
add("https://cifar.ca/cifarnews/2026/06/04/statement-on-canadas-national-ai-strategy/",
    "Statement on Canada's National AI Strategy", "CIFAR", "2026-06-04", "Canada", "statement", ["policy","research","funding"],
    "CIFAR welcomes the renewed strategy and plans to scale the Canada CIFAR AI Chairs cohort to nearly 200.", author="Toope, S. J.")
add("https://mila.quebec/en/news/canadas-national-ai-strategy-mila-welcomes-an-ambitious-vision-propelling-canada-toward",
    "Canada's National AI Strategy: Mila welcomes an ambitious vision propelling Canada toward scientific and technological leadership",
    "Mila – Quebec Artificial Intelligence Institute", "2026-06-04", "Canada", "statement", ["policy","research","indigenous"],
    "Mila highlights the strategy's six pillars, the expanded AI Chairs program, the First Languages AI Reality (FLAIR) program for Indigenous leadership, and a Cohere partnership on Quebec French-language AI.")
add("https://www.amii.ca/updates-insights/ai-for-all-national-ai-strategy",
    "AI for All: Canada's National AI Strategy", "Alberta Machine Intelligence Institute (Amii)", "2026-06-04", "Canada", "statement",
    ["policy","education-k12","literacy","workforce"],
    "Strategy shaped by 11,000+ consultation submissions. Amii outlines its K-12 AI Learning Kits ($2.7M Alberta partnership) and AI Workforce Readiness program.", author="Vang, L.")
add("https://actua.ca/news-views/ai-strategy-statement",
    "Actua welcomes youth AI literacy in Canada's National AI Strategy as a first step toward building Canada's AI-ready workforce",
    "Actua", "2026-06-04", "Canada", "statement", ["policy","funding","youth","literacy","stem-outreach"],
    "Actua welcomes youth AI literacy in the strategy and the $30M CanCode investment, but notes Canada ranks 42nd of 47 countries on AI literacy/training and that CanCode funding is lower than in previous rounds.")
add("https://www.bakermckenzie.com/en/insight/publications/2026/06/canada-federal-government-releases-refreshed-national-ai-strategy",
    "Canada: Federal government releases refreshed national AI strategy", "Baker McKenzie", "2026-06-09", "Canada", "analysis",
    ["policy","funding","workforce"],
    "Outlines six priorities and five priority sectors; cites a $500M Tech Growth Fund, $700M more for the Compute Access Fund and a $200M healthcare AI mission.")
add("https://vectorinstitute.ai/vector-welcomes-canadas-ai-strategy-ai-for-all/",
    "Vector welcomes Canada's AI Strategy: AI for All", "Vector Institute", "2026-06-09", "Canada", "statement", ["policy","literacy","research"],
    "Vector welcomes the strategy and highlights the national AI literacy initiative and FastLane startups introduced at the launch.", author="Williams, K.")
add("https://www.dlapiper.com/en/insights/publications/2026/06/canada-unveils-national-ai-strategy",
    "Canada unveils national AI strategy: Key commitments, regulatory gaps, and what's missing", "DLA Piper", "2026-06-12", "Canada", "analysis",
    ["policy","funding","workforce","safety"],
    "Up to 250,000 new AI-relevant jobs targeted by 2031 and a $500M Canadian Tech Growth Fund; no standalone AI legislation planned and no timelines for privacy or online-safety bills.",
    author="Black, R., McDonald, M., Schaffrick, M., & Singh, S.")
add("https://culturalpolicyhub.ocadu.ca/news/canadas-national-ai-strategy-key-overview-and-what-it-means-canadas-arts-culture-and-heritage",
    "Canada's National AI Strategy: Key overview and what it means for Canada's arts, culture, and heritage sector and creative industries",
    "Cultural Policy Hub, OCAD University", "", "Canada", "analysis", ["culture","creative","policy"],
    "Reviews the strategy for the arts sector: a $50M Creative Technology Program and a planned Advisory Council on AI and Culture; notes the strategy does not address IP used to train generative AI.",
    author="Godbillon-Vasseur, C., & Kramer, M.")
add("https://www.canada.ca/en/innovation-science-economic-development/news/2026/07/government-of-canada-invests-30-million-to-launch-fifth-phase-of-cancode-program-to-offer-new-training-opportunities-for-youth-and-teachers.html",
    "Government of Canada invests $30 million to launch fifth phase of CanCode program to offer new training opportunities for youth and teachers",
    "Innovation, Science and Economic Development Canada", "2026-07-08", "Canada", "announcement",
    ["funding","education-k12","teachers","youth","stem-outreach"],
    "CanCode phase five: $30M to reach 1.1 million students and train 76,000 teachers in digital skills, coding and AI. Applications open to not-for-profits.")
add("https://vectorinstitute.ai/?p=26983", "Ontario's AI ecosystem snapshot 2025/2026", "Vector Institute", "2026-08-17", "Canada", "report",
    ["funding","workforce","research"],
    "121 new Ontario AI companies (+73%), $3.9B private VC (+50%), $796M AI R&D funding, and 71,167 non-technical jobs requiring AI skills (+61%).", author="Williams, K.")
add("https://www.canada.ca/en/innovation-science-economic-development/news/2026/09/government-of-canada-launches-national-ai-literacy-initiative.html",
    "Government of Canada launches National AI Literacy Initiative", "Innovation, Science and Economic Development Canada", "2026-09-09", "Canada", "announcement",
    ["literacy","education-k12","post-secondary","adult-education","teachers"],
    "National AI Literacy Initiative with Amii aims to reach up to one million post-secondary students and 50,000+ K-12 educators, with a free three-hour course and an 'Essentials for Canadians' stream.")
add("https://www.amii.ca/updates-insights/amii-leads-national-ai-literacy-initiative",
    "Amii leads National AI Literacy Initiative to empower 1 million learners", "Alberta Machine Intelligence Institute (Amii)", "2026-09-09", "Canada", "announcement",
    ["literacy","education-k12","post-secondary","teachers","adult-education"],
    "Three learning streams (students, educators, all Canadians), formal launch September 21, 2026. Amii reports 1.3 million learners reached worldwide.", author="Vang, L.")
add("https://www.hcamag.com/ca/specialization/transformation/ai-work-placements-ottawa-funds-10000-spots-for-young-canadians/591583",
    "AI work placements: Ottawa funds 10,000 spots for young Canadians", "HRD Canada", "2026-09-29", "Canada", "news",
    ["workforce","funding","post-secondary","youth"],
    "ISED to provide up to $162M over five years to Mitacs for 10,000 co-funded AI work placements for students, graduates and postdocs.", author="Wilson, J.")
add("https://thehub.ca/2026/09/30/canadas-ai-minister-outlines-his-vision-for-balancing-innovation-and-safety/",
    "Canada's AI minister outlines his vision for balancing innovation and safety", "The Hub", "2026-09-30", "Canada", "news",
    ["policy","safety","ethics"],
    "Minister Evan Solomon frames trust and safety as foundations for adoption; notes 150,000+ Canadians work in AI and a goal of raising adoption from 12% to 60%.")
add("https://www.bnnbloomberg.ca/business/politics/2026/11/05/feds-to-spend-1-billion-on-digital-transformation-of-public-service/",
    "Feds to spend $1 billion on digital transformation of public service", "BNN Bloomberg / CTV News", "2026-11-05", "Canada", "news",
    ["funding","policy","workforce"],
    "Budget 2026 creates a $1B Government Transformation Fund and Digital Transformation Canada to lead public-service AI adoption.", author="Pringle, J.")
add("https://www.hcamag.com/ca/specialization/transformation/canadas-2026-federal-budget-bets-on-building-a-workforce-from-within/596514",
    "Canada's 2026 federal budget bets on building a workforce from within", "HRD Canada", "2026-11-06", "Canada", "news",
    ["workforce","funding","policy","indigenous"],
    "Budget 2026 workforce measures include an apprenticeship service and $451.8M over four years for a Partnerships for Indigenous Workforce Readiness Fund.", author="Smith, J. R.")

# ---------- Canada: schools, teachers, post-secondary ----------
add("https://techpolicy.press/canadas-ai-strategy-must-address-the-technologys-use-in-k12-education",
    "Canada's AI strategy must address the technology's use in K-12 education", "Tech Policy Press", "2026-05-14", "Canada", "opinion",
    ["policy","education-k12","safety","literacy"],
    "Argues the national strategy must cover K-12, proposing AI literacy plus governance for youth safety, cybersecurity and privacy; few provinces or boards have responsible-use policies.", author="Côté, A., & Naylor, N.")
add("https://ontariosuniversities.ca/news/charting-a-path-forward-for-ontario-universities-in-the-age-of-ai/",
    "Charting a path forward for Ontario universities in the age of AI", "Council of Ontario Universities", "2026-05-29", "Canada", "report",
    ["post-secondary","policy","workforce","ethics"],
    "COU AI Task Force (chair Vivek Goel) report sets four pillars: preparing students and workforce, industry partnership, responsible AI across teaching/research/operations, and public trust.", author="Hoang, C.")
add("https://educationnewscanada.com/article/organization/17565/1205490/Canadian-Teachers-Federation-Calls-for-Stronger-K-12-Protections-in-National-AI-Strategy-.htm",
    "Canadian Teachers' Federation calls for stronger K-12 protections in national AI strategy", "Canadian Teachers' Federation (via Education News Canada)", "2026-06-09", "Canada", "statement",
    ["policy","education-k12","teachers","safety"],
    "CTF/FCE (370,000+ educators) says the strategy's teacher-training commitment covers only 3,000 of 420,000 public educators; calls for safety-by-design, independent impact assessments and procurement standards.")
add("https://www.torontomu.ca/diversity/news-events/2026/08/new-national-study-young-canadians-embrace-ai-but-see-ai-generated-work-as-cheating/",
    "Young Canadians embrace AI but see AI-generated work as cheating: New national study", "Diversity Institute, Toronto Metropolitan University", "2026-08-06", "Canada", "research",
    ["youth","ethics","research"],
    "National survey (ACS-AEC, Metropolis Institute, Diversity Institute): only 45% of AI users disclose use at work/school, though ~75% support disclosure for schoolwork.")
add("https://thehub.ca/2026/08/28/canadian-teachers-say-ai-is-doing-students-homework-and-their-thinking/",
    "Canadian teachers overwhelmingly say AI is doing students' homework and critical thinking skills are declining: Study", "The Hub", "2026-08-28", "Canada", "news",
    ["teachers","education-k12","research","youth"],
    "Fraser Institute/Leger survey of 756 grade 6–12 teachers: 95.6% think some students use AI on take-home work; 83.6% see declining critical thinking over five years.", author="Gordon, G.")
add("https://www.fraserinstitute.org/sites/default/files/2026-08/survey-of-canadian-grades-6-12-teachers-on-ai-use.pdf",
    "Survey of Canadian grades 6–12 teachers on AI use", "Fraser Institute", "2026-08", "Canada", "research",
    ["education-k12","teachers","research"],
    "Leger poll of 756 teachers (Nov 2025–Jan 2026) on student AI use, academic integrity and critical thinking.", author="MacPherson, P.")
add("https://kpmg.com/ca/en/media/2026/09/majority-of-students-use-ai-but-educators-sound-alarm.html",
    "Majority of students use AI, but educators sound alarm", "KPMG Canada", "2026-09-04", "Canada", "research",
    ["post-secondary","education-k12","teachers","research"],
    "Survey of 1,009 students and educators: 75% of students use generative AI for schoolwork; 59% of educators say the system is not preparing students for an AI-enabled workplace.")
add("https://www.ctvnews.ca/sci-tech/article/wild-west-teachers-experts-call-for-unified-policies-to-address-ai-in-classrooms",
    "'Wild West': Teachers, experts call for unified policies to address AI in classrooms", "CTV News / The Canadian Press", "2026-09-04", "Canada", "news",
    ["policy","education-k12","teachers"],
    "Teachers and experts call for a consistent national framework for classroom AI as Ottawa pushes broad adoption.")
add("https://www.educationnewscanada.com/article/education/level/k12/3/1215572/policies-to-protect-students-educators-and-public-education-in-the-ai-age-.html",
    "Policies to protect students, educators, and public education in the AI age", "Canadian Teachers' Federation (via Education News Canada)", "2026-09-28", "Canada", "report",
    ["policy","education-k12","safety","ethics","teachers"],
    "CTF policy brief on student/educator data, cognitive offloading, AI chatbots and companions, and unregulated adoption; recommends sensitive-by-default data rules, critical AI literacy and public digital platforms.")
add("https://www.educationnewscanada.com/article/education/level/k12/3/1223177/canadian-teachers-federation-concerned-national-ai-literacy-initiative-puts-adoption-before-safety.html",
    "Canadian Teachers' Federation concerned National AI Literacy Initiative puts adoption before safety", "Canadian Teachers' Federation (via Education News Canada)", "2026-10-15", "Canada", "statement",
    ["policy","teachers","ethics","safety","literacy"],
    "CTF says the initiative asks teachers to adopt AI before its learning safety is known and that the 50,000-educator target lacks an impact-measurement plan.")
add("https://www.amii.ca/updates-insights/amii-delivers-ai-literacy-programs-to-accec-to-empower-young-black-founders",
    "Amii delivers AI programs to African Canadian Civic Engagement Council to empower young Black founders", "Alberta Machine Intelligence Institute (Amii)", "2026-06-29", "Canada", "announcement",
    ["black-communities","workforce","community","literacy"],
    "Through ACCEC's ANZA 2.0 program, Amii will deliver 10 private Machine Learning Exploration cohorts over five years plus access to AI Literacy for Everyone.", author="Vang, L.")
add("https://www.amii.ca/updates-insights/celebrating-10-years-of-the-ai4good-lab-edmonton",
    "Celebrating 10 years of the AI4Good Lab & Edmonton's standout cohort", "Alberta Machine Intelligence Institute (Amii)", "2026-08-11", "Canada", "news",
    ["stem-outreach","workforce","youth"],
    "The seven-week AI4Good Lab (Amii, Mila, Vector) marked 10 years: 85 women and gender-diverse participants, 14 teams presenting prototypes at the Montreal Demo Day.", author="Vang, L.")

# ---------- Indigenous AI & Indigenous futurism ----------
add("https://mila.quebec/en/news/mila-and-cifar-launch-the-indigenous-ai-advisory-circle",
    "Mila and CIFAR launch the Indigenous AI Advisory Circle", "Mila & CIFAR", "2026-05-26", "Canada", "announcement",
    ["indigenous","policy","community"],
    "Six Indigenous leaders will guide Indigenous participation in Canada's AI ecosystem, informing initiatives at CIFAR, Mila, Amii and Vector.")
add("https://mila.quebec/en/news/discover-the-third-cohort-of-indigenous-pathfinders-in-ai",
    "Discover the third cohort of Indigenous Pathfinders in AI", "Mila – Quebec Artificial Intelligence Institute", "2026-05-28", "Canada", "announcement",
    ["indigenous","workforce","community","adult-education"],
    "Seven-week program in Montréal with workshops and mentoring for Indigenous participants from engineering, arts, health, journalism and entrepreneurship working on community projects.")
add("https://educationnewscanada.com/article/education/region/quebec/26/1210837/concordia-universityjuly-13-2026-skawennati-brings-indigenous-futurism-to-montreal-s-streets.html",
    "Skawennati brings Indigenous futurism to Montreal's streets", "Concordia University (via Education News Canada)", "2026-07-13", "Canada", "creative",
    ["indigenous-futurism","indigenous","creative","culture"],
    "Skawennati's augmented-reality façade work for the Conseil des arts de Montréal's 70th anniversary reimagines the Three Sisters as superheroes.")
add("https://www.arctictoday.com/%F0%9F%87%A8%F0%9F%87%A6-mila-and-polarctic-canada-announce-partnership-to-advance-ai-powered-sea-ice-forecasting-in-the-canadian-arctic/",
    "Mila and PolArctic Canada announce partnership to advance AI-powered sea ice forecasting in the Canadian Arctic", "ArcticToday", "2026-07-16", "Canada", "announcement",
    ["indigenous","research","community"],
    "Announced at Mila's 2026 Indigenous AI Gathering: PolArctic's forecasting combines Inuit knowledge, ocean science and satellite data.", author="Thorsson, E.")
add("https://mila.quebec/en/news/indigenous-pathfinders-in-ai-discover-the-third-cohorts-ideas-in-action",
    "Indigenous Pathfinders in AI: Discover the third cohort's ideas in action", "Mila – Quebec Artificial Intelligence Institute", "2026-09-02", "Canada", "news",
    ["indigenous","community","workforce"],
    "At the July 16 Pitch Day (Indigenous AI Gathering 2026), six teams showed prototypes in language revitalization, health, education and data sovereignty; LandLens and SAI Cheese won Mila residencies.")
add("https://sciencepolicy.ca/posts/building-canadas-ai-advantage-through-indigenous-innovation/",
    "Building Canada's AI advantage through Indigenous innovation", "Canadian Science Policy Centre", "2026-09-05", "Canada", "opinion",
    ["indigenous","policy","funding"],
    "Urges AI for All to embed Indigenous knowledge and leadership and channel funding, procurement and venture capital to Indigenous-led AI and data sovereignty.", author="Canavera, L., & Chartrand, L.")
add("https://sciencepolicy.ca/posts/who-actually-decides/",
    "Who actually decides? The sovereignty test \"AI for All\" must pass", "Canadian Science Policy Centre", "2026-09-07", "Canada", "opinion",
    ["policy","indigenous"],
    "Links First Nations water legislation and cloud-sovereignty debates to AI for All, arguing sovereignty means decision rights over land, energy and water used by AI infrastructure.", author="Maleki, K.")
add("https://www.educationnewscanada.com/article/education/category/research/100/1225479/simon-fraser-universityoctober-29-2026-flair-project-at-sfu-harnesses-ai-to-revive-indigenous-languages.html",
    "FLAIR project at SFU harnesses AI to revive Indigenous languages", "Simon Fraser University (via Education News Canada)", "2026-10-29", "Canada", "research",
    ["indigenous","research","culture"],
    "First Languages AI Reality (FLAIR), at SFU's Digital Democracies Institute, builds AI learning modules and speech tools with the Gwich'in, Kwakwaka'wakw, Makah and Yawanawá.")

# ---------- Black communities, Afrofuturism, ethics ----------
add("https://democracynow.org/2026/8/13/timnit_gebru",
    "\"Deep unlearning\": Timnit Gebru on AI hype, ethics & algorithmic racial bias", "Democracy Now!", "2026-08-13", "International", "video",
    ["ethics","black-communities"],
    "Interview with DAIR founder and Black in AI co-founder Timnit Gebru on AI hype, ethics and racial bias.")
add("https://www.bnnbloomberg.ca/press-releases/2026/06/30/vector-institute-releases-unbias-plus-a-free-open-source-ai-tool-to-detect-and-rewrite-bias-in-text/",
    "Vector Institute releases UnBias-Plus, a free, open-source AI tool to detect and rewrite bias in text", "Vector Institute (GlobeNewswire)", "2026-06-30", "Canada", "announcement",
    ["ethics","research"],
    "Open-source tool from Vector's AI Safety researchers detects, explains and rewrites biased language in text and training datasets (English only).")
add("https://montrealethics.ai/saier-vol-8-landing/",
    "State of AI Ethics Report, Volume 8", "Montreal AI Ethics Institute", "2026-11", "Canada", "report",
    ["ethics","policy","research","community"],
    "CC BY 4.0 report on how power over AI was exercised in 2026 and where governance fell short; 62 contributions from 91 contributors worldwide.", author="Butalid, R., & Wright, C. (Eds.)")
add("https://culturalpolicyhub.ocadu.ca/sites/default/files/report-pdfs/Hub_ArtsEtobicoke_AI_ArtistsAIandPolicyEvent_July2026_SummaryReport_EN.pdf",
    "Summary report: The Cultural Policy Hub x Arts Etobicoke artists, AI and policy roundtable", "Cultural Policy Hub (OCAD U) & Arts Etobicoke", "2026-07-21", "Canada", "report",
    ["creative","policy","literacy","community"],
    "Report of a July 21, 2026 roundtable: four themes — artistic agency and transparency, accountability, AI literacy, and artists' role in policymaking.")
add("https://research.google/pubs/meet-the-ai-moment-using-afrofuturism-and-technowomanism-together-as-technological-practice/",
    "Meet the AI moment: Using Afrofuturism and technowomanism together as technological practice", "ACM Designing Interactive Systems (DIS 2026) workshop", "2026", "International", "research",
    ["afrofuturism","black-communities","creative","research"],
    "Two-day DIS 2026 workshop framing AI design through Afrofuturism and technowomanism, aiming at a toolkit centring People of the Global Majority.",
    author="Bosley, B., Klassen, S., Harrington, C., Asare, I., Almeida, F., Idaewor, H., & Salih, Y.", background=True)
add("https://carleton.ca/africanstudies/2026/being-black-in-ai-evidence-trends-and-policy-futures-at-the-intersection-of-artificial-intelligence-and-african-caribbean-and-black-communities-in-canada",
    "Being Black in AI: Evidence, trends, and policy futures at the intersection of artificial intelligence and African, Caribbean, and Black communities in Canada",
    "CanAfro Research Institute (via Carleton Institute of African Studies)", "2026-02-13", "Canada", "report",
    ["black-communities","policy","research","workforce"],
    "Volunteer-led report on how ACB communities are positioned in Canada's AI labour market, innovation strategy and governance, with policy recommendations.", background=True)
add("https://www.torontomu.ca/law/news-events/2026/02/black-futures-by-design-advancing-racial-justice-in-canadas-ai-governance/",
    "Black futures by design: Advancing racial justice in Canada's AI governance", "Lincoln Alexander School of Law, Toronto Metropolitan University", "2026-02-21", "Canada", "report",
    ["black-communities","policy","ethics","afrofuturism"],
    "Argues AI reproduces racial inequities in justice, employment and finance; identifies missing transparency, accountability and community oversight.", author="Effoduh, J. O.", background=True)
add("https://maxpolicy.substack.com/p/without-black-voices-canadas-ai-strategy",
    "Without Black voices, Canada's AI strategy is already broken", "maxpolicy (Substack)", "", "Canada", "opinion",
    ["black-communities","policy","ethics"],
    "Notes the 27-member AI Strategy Task Force had no Black members, cites a letter from 60 Black Canadian scholars and proposes an equity and accountability subcommittee.", author="Afowork, H.")
add("https://warwick.ac.uk/fac/cross_fac/eduport/edufund/projects/yang/projects/reimagining-ai-exploring-speculative-design-workshops-for-supporting-bipoc-youth-critical-ai-6747a1/",
    "Reimagining AI: Exploring speculative design workshops for supporting BIPOC youth critical AI literacies", "University of Warwick", "", "International", "research",
    ["black-communities","youth","ethics","stem-outreach","afrofuturism"],
    "Speculative-design workshops on AI ethics inside an 8-week Black-led AI STEAM program for grade 9–12 students.", author="Kenny, S., & Antle, A. N.", background=True)
add("https://www.royalgreenwich.gov.uk/events/create-future-heads-young-voices-black-heritage-ai-futures-3",
    "Future Heads: Young voices, Black heritage, AI futures!", "Royal Borough of Greenwich / Create", "", "UK", "event",
    ["black-communities","youth","creative","afrofuturism"],
    "Free youth workshop series (spoken word, digital art, media design) on identity, Black heritage and AI futures.", background=True)

# ---------- UK ----------
add("https://www.computingatschool.org.uk/forum-news-blogs/2026/may/state-of-the-nation-ai-in-education-what-educators-need-to-know/",
    "State of the nation: AI in education – what educators need to know", "Computing at School (BCS)", "2026-05-15", "UK", "analysis",
    ["teachers","education-k12","policy"],
    "76% of teachers use AI day to day; 49% of schools reportedly lack an AI policy; 21% of state-school teachers have formal AI training vs 45% in private schools.", author="Peters, B.")
add("https://www.resultsense.com/news/2026-05-21-uk-public-ai-fear-jobs-civil-unrest-kcl-study/",
    "UK workers and bosses split on AI: KCL study finds one in five fear civil unrest", "Resultsense", "2026-05-21", "UK", "research",
    ["workforce","research","policy"],
    "King's College London study: 70% of Britons worry about AI's economic impact; 69% of employers vs 28% of the public are optimistic about AI job creation.")
add("https://workplacejournal.co.uk/2026/06/government-launches-ai-jobs-scheme-for-young-people/",
    "Government launches AI jobs scheme for young people", "Workplace Journal", "2026-06-08", "UK", "news",
    ["workforce","funding","youth","education-k12"],
    "UK Early Careers Jobs Alliance (£20M); TechFirst to give AI and tech training to at least 400,000 students from disadvantaged schools.", author="O'Connor, J.")
add("https://efi.ed.ac.uk/citizens-assembly-key-to-giving-public-a-voice-on-ai/",
    "Citizens' assembly key to giving public a voice on AI", "Edinburgh Futures Institute", "2026-06-09", "UK", "report",
    ["policy","community"],
    "'Governing the Future' report from the Edinburgh Data and AI Exchange recommends a standing UK citizens' assembly on AI and society.", author="Macapagal, K.")
add("https://connectedbydata.org/blog/2026/06/29/cop-summary",
    "Data and AI Public Engagement Community of Practice – a summary", "Connected by Data", "2026-06-29", "UK", "analysis",
    ["community","research"],
    "Wrap-up of a two-year community of practice (17 events) for people running public engagement on data and AI.", author="Freeguard, G.")
add("https://efi.ed.ac.uk/edinburgh-futures-institute-and-phoenix-court-deliver-ai-literacy-challenge/",
    "Edinburgh Futures Institute and Phoenix Court deliver AI Literacy Challenge", "Edinburgh Futures Institute", "2026-08-12", "UK", "news",
    ["adult-education","community","literacy"],
    "Community AI literacy pilot (four tutor-led sessions) with the Grassmarket Community Project in July 2026; more cohorts planned for winter 2026–27.", author="Macapagal, K.")
add("https://www.gov.uk/government/news/ai-bootcamp-launched-in-north-west-to-combat-youth-unemployment",
    "AI bootcamp launched in north-west to combat youth unemployment", "GOV.UK", "2026-08-14", "UK", "announcement",
    ["workforce","youth","adult-education"],
    "Three-week AI bootcamp for up to 70 people aged 16–21 (IN4 Group) with apprenticeships; it will inform an England-wide AI skills scheme next summer.")
add("https://www.resultsense.com/news/2026-09-22-seldon-report-ai-schools-framework/",
    "Seldon report says English schools need a national AI plan", "Resultsense", "2026-09-22", "UK", "news",
    ["policy","education-k12","teachers"],
    "Report by Sir Anthony Seldon and Tim Bunting proposes a 10-point plan, including an Ofsted-checked AI strategy in every school.")
add("https://www.gov.uk/government/news/450000-disadvantaged-pupils-could-benefit-from-ai-tutoring-tools",
    "450,000 disadvantaged pupils could benefit from AI tutoring tools", "Department for Education (UK)", "2026-01-26", "UK", "announcement",
    ["education-k12","policy","funding","teachers"],
    "AI tutoring tools co-created with teachers for up to 450,000 disadvantaged pupils by end-2027; £23M to expand EdTech Testbeds to 1,000+ schools.", background=True)
add("https://institute.global/insights/public-services/generation-ready-scaling-safe-high-quality-ai-englands-schools",
    "Generation ready: Scaling safe, high-quality AI in England's schools", "Tony Blair Institute for Global Change", "2026-01-22", "UK", "report",
    ["policy","education-k12","teachers"],
    "Only 10% of state secondaries teach pupils to use AI in subjects; proposes a free national AI teaching assistant and an AI Readiness Fund.", author="Crowley-Carbery, K., & West, E.", background=True)

# ---------- EU & international ----------
add("https://education.ec.europa.eu/node/3537",
    "New AI Literacy Framework helps schools prepare learners for the age of artificial intelligence", "European Commission (European Education Area)", "2026-06-18", "EU", "announcement",
    ["policy","education-k12","teachers","literacy"],
    "European Commission and OECD AI Literacy (AILit) Framework for primary and secondary education: 4 dimensions, 19 competences, classroom examples.")
add("https://ki-campus.org/en/blog/eu-ai-act-ai-omnibus-recalibrates-article-4-ai-literacy-remains-mandatory",
    "EU AI Act: AI Omnibus recalibrates Article 4 – AI literacy remains mandatory", "KI-Campus (Stifterverband)", "2026-07-28", "EU", "analysis",
    ["policy","workforce","literacy"],
    "Article 4 kept but softened: providers and deployers must support AI literacy without guaranteeing a set competence level; the AILit Framework is a reference point.")
add("https://www.raspberrypi.org/blog/supporting-ai-education-for-150000-learners-in-aotearoa-new-zealand-and-australia/",
    "Supporting AI education for 150,000 learners in Aotearoa New Zealand and Australia", "Raspberry Pi Foundation", "2026-08-04", "International", "announcement",
    ["stem-outreach","teachers","education-k12","indigenous"],
    "Experience AI expands to train 5,000 educators reaching 150,000 students by 2028 ($1.2M Google.org), with partners including Tōnui Collab Charitable Trust.", author="Burton, A.")
add("https://www.brusselstimes.com/2328535/europes-classrooms-face-mixed-results-as-generative-ai-reshapes-learning",
    "Europe's classrooms face mixed results as generative AI reshapes learning", "The Brussels Times", "2026-09-22", "EU", "news",
    ["research","policy","teachers"],
    "Two Commission reports find generative AI becoming mainstream in learning, with outcomes depending on use; teachers need substantial initial and ongoing training.")
add("https://portugalglobal.pt/en/news/2026/setembro/eu-examines-impact-of-generative-ai-on-education/",
    "EU examines impact of generative AI on education", "AICEP Portugal Global", "2026-09-23", "EU", "news",
    ["research","policy"],
    "Covers the Commission's 'Friend or foe?' and 'Digital education at school in Europe 2026' reports; nearly two-thirds of systems have AI strategies or guidance.")
add("https://www.euronews.com/2026/11/05/eu-plans-to-deliver-ai-literacy-certificates-to-students",
    "EU plans to deliver 'AI literacy' certificates to students", "Euronews", "2026-11-05", "EU", "news",
    ["policy","education-k12","youth","literacy"],
    "EU working on an AI literacy certificate for 15-year-olds from the 2027–28 school year, to help pupils understand AI, check outputs and spot manipulation.", author="Camba, G.")

# ---------- Background context (before the window) ----------
add("https://actua.ca/news-views/ai-report",
    "AI skills gap: Youth confident, educators need support, Actua report reveals", "Actua", "2025-06-23", "Canada", "research",
    ["youth","teachers","education-k12","literacy","research"],
    "Abacus surveys of 502 educators and 1,000 youth (12–18): 84% of youth say they have more to learn about AI; only 48% of educators feel skilled using AI in class.", background=True)
add("https://actua.ca/news-views/2026-cancode-renewal",
    "Actua welcomes CanCode renewal as foundation for Canada's digital and AI future", "Actua", "2026-04-29", "Canada", "statement",
    ["funding","stem-outreach","youth"],
    "CanCode renewed in the Spring Economic Update; Actua's network has engaged 3.7M+ youth, focusing on Indigenous youth, girls and rural/remote communities.", background=True)
add("https://amii.ca/updates-insights/amii-partners-with-alberta-government-to-bring-ai-literacy-to-k-12-classrooms",
    "Amii partners with Alberta government to bring AI literacy to K-12 classrooms", "Alberta Machine Intelligence Institute (Amii)", "2026-04-29", "Canada", "announcement",
    ["funding","education-k12","teachers","literacy"],
    "Three-year, $2.7M partnership for provincial AI learning kits by spring 2028; Amii's K-12 program has trained 5,000 teachers and reached 127,000+ students.", author="Vang, L.", background=True)
add("https://www.torontomu.ca/diversity/news-events/2026/05/rethinking-ai-skills-why-stem-alone-wont-prepare-us-for-whats-ahead/",
    "Rethinking AI skills: Why STEM alone won't prepare us for what's ahead", "Diversity Institute, Toronto Metropolitan University", "2026-04-22", "Canada", "analysis",
    ["workforce","stem-outreach","literacy"],
    "Wendy Cukier argues Canada lags on adoption and that AI skills should not be STEM-only: AI literacy for all plus humanities and social-science skills.", background=True)
add("https://durhamcollege.ca/new-notable/college-news/durham-college-ai-hub-partners-with-ecampusontario-to-deliver-free-learning-modules-across-canada",
    "Durham College AI Hub partners with eCampusOntario to deliver free learning modules across Canada", "Durham College", "2026-02-23", "Canada", "announcement",
    ["post-secondary","adult-education","literacy"],
    "Free, bilingual seven-module AI Fundamentals micro-credential series (20–30 minutes per module).", background=True)
add("https://educationnewscanada.com/article/education/level/k12/3/1198801/how-should-schools-teach-ai-3-models-to-consider.html",
    "How should schools teach AI? 3 models to consider", "The Conversation (via Education News Canada)", "2026-05-05", "Canada", "analysis",
    ["education-k12","literacy","policy"],
    "Asks what AI literacy students need and where it belongs in curriculum, noting Canada has no single approach because education is provincial.", background=True)
add("https://dayofai.org/program-hubs/canada", "Day of AI – Canada program hub", "Day of AI (MIT RAISE)", "", "Canada", "resource",
    ["youth","education-k12","stem-outreach","literacy"],
    "Actua has adapted the Day of AI curriculum for Canadian youth through its AI Ready project.", background=True)
add("https://www.digitalmoment.org/news/free-classroom-ready-coding-and-ai-lessons-for-k-12-educators",
    "Free classroom-ready lessons for K–12 educators", "Digital Moment", "2026", "Canada", "resource",
    ["education-k12","teachers","stem-outreach","literacy"],
    "Free K–12 coding and AI lessons (most under an hour, no coding experience needed) from an organisation that has trained 34,400 educators.", background=True)

# ---------- Gap-fill pass (institute news listings + targeted checks) ----------
# Items marked "(listing)" were verified from the publisher's dated news listing; summaries stay close to the listed title/blurb.
add("https://www.adalovelaceinstitute.org/press-release/ai-public-sector-productivity/",
    "Policymakers must apply higher standards of evidence to claims about AI and public sector productivity, says the Ada Lovelace Institute",
    "Ada Lovelace Institute", "2026-05-11", "UK", "statement", ["policy","research"],
    "New briefing to help policymakers and journalists critically evaluate claims about AI and public-sector productivity.")
add("https://www.unitedforliteracy.ca/About/News/What-artificial-intelligence-means-adult-literacy-Canada",
    "Reading the future: What artificial intelligence means for adult literacy in Canada", "United for Literacy", "2026-06-03", "Canada", "opinion",
    ["adult-education","literacy","ethics"],
    "One in five working-age Canadians struggles with basic literacy; argues AI can personalise adult learning but brings risks of bias, data exposure and over-dependence.", author="Valcin, M.")
add("https://www.raspberrypi.org/blog/ai-education-resources-ai-awareness-day/",
    "Support your young people with our AI literacy resources", "Raspberry Pi Foundation", "2026-06-03", "UK", "resource",
    ["literacy","teachers","education-k12"], "Free AI literacy resources to help educators worldwide teach AI with confidence (listing).", author="Hutchings, J.")
add("https://globalnews.ca/news/11891996/canada-ai-strategy-kindergarten-learning/",
    "Should AI training start in kindergarten? What we know about Ottawa's plan", "Global News", "2026-06-05", "Canada", "news",
    ["policy","education-k12","literacy","funding"],
    "The strategy commits $30M to CanCode for K–12 digital and AI skills, but gives little detail on what kindergarten AI training means; curriculum remains provincial.", author="Rana, U.")
add("https://actua.ca/news-views/safe-social-media-act",
    "Actua applauds Bill C-34, urges greater investment in digital and AI literacy", "Actua", "2026-06-11", "Canada", "statement",
    ["policy","safety","literacy","youth"],
    "Actua welcomes Bill C-34 as a step toward a safer digital world for young Canadians but says regulation must be matched by investment in digital and AI literacy.")
add("https://ubyssey.ca/news/canadas-federal-ai-strategy-for-students/",
    "Here's what Canada's AI strategy could mean for students", "The Ubyssey", "2026-06-11", "Canada", "news",
    ["policy","post-secondary","literacy","youth"],
    "Strategy promises AI training for every post-secondary student; UBC's Heidi Tworek notes few insights on regulation and safeguards.", author="Jian, S.")
add("https://educationnewscanada.com/article/organization/32271/1206474/Beyond-literacy-students-need-to-be-fluent-with-AI-.htm",
    "Canada's AI strategy and universities: Beyond literacy, students need to be fluent with AI", "The Conversation (via Education News Canada)", "2026-06-15", "Canada", "analysis",
    ["policy","post-secondary","literacy"],
    "Argues universities must move students past basic AI literacy to fluency, noting criticism of the strategy's thin detail on safety and governance.")
add("https://www.educationnewscanada.com/article/education/level/university/1/1206661/new-federal-ai-strategy-emphasizes-university-research-training-and-commercialization-.html",
    "New federal AI strategy emphasizes university research, training and commercialization", "University Affairs (via Education News Canada)", "2026-06-19", "Canada", "news",
    ["policy","post-secondary","research","literacy"],
    "Canada CIFAR AI Chairs to rise from 143 to nearly 200; universities given roles in research, commercialisation and AI literacy training.")
add("https://www.digitalmoment.org/news/digital-moment-and-the-canadian-commission-for-unesco-launch-a-national-ai-literacy-hub-for-youth-in-canada",
    "National AI Literacy Hub for Youth in Canada", "Digital Moment & Canadian Commission for UNESCO", "2026-06-22", "Canada", "resource",
    ["youth","literacy","teachers"],
    "'AI in Your Everyday Life': a bilingual hub for youth 13–18 with games, a glossary, educator and family guides, and short documentaries.")
add("https://www.amii.ca/updates-insights/ai-workforce-readiness-program-expands-curriculum-focus",
    "Amii's AI Workforce Readiness program expands curriculum focus", "Alberta Machine Intelligence Institute (Amii)", "2026-06-25", "Canada", "announcement",
    ["workforce","post-secondary","literacy","teachers"],
    "Five new curriculum packages for post-secondary instructors (e.g., AI in Accounting), a three-hour 'Module 0' AI literacy unit, and a consortium of 57 institutions.", author="Vang, L.")
add("https://mila.quebec/en/news/mila-and-roost-launch-suicide-prevention-guardrail-pilot-to-help-make-ai-chatbots-safer-for",
    "Mila and ROOST launch suicide prevention guardrail pilot to help make AI chatbots safer for youth", "Mila – Quebec Artificial Intelligence Institute", "2026-07-08", "Canada", "announcement",
    ["safety","youth","ethics"], "Pilot of a suicide-prevention guardrail aimed at making AI chatbots safer for young people (listing).")
add("https://www.amii.ca/updates-insights/alberta-invests-50m-in-amii-to-drive-impact",
    "Putting Alberta's AI advantage to work: Alberta invests $50M in Amii to drive impact", "Alberta Machine Intelligence Institute (Amii)", "2026-07-09", "Canada", "announcement",
    ["funding","policy"], "Alberta government invests $50M in Amii (listing).")
add("https://mila.quebec/en/news/disinformation-20-in-the-age-of-artificial-intelligence",
    "Disinformation 2.0 in the age of artificial intelligence", "Mila – Quebec Artificial Intelligence Institute", "2026-07-17", "Canada", "analysis",
    ["ethics","safety","literacy"], "Mila piece on AI-driven disinformation (listing).")
add("https://www.digitalmoment.org/news/youth-ai-literacy",
    "Youth AI literacy: What kids and teens need to know about AI", "Digital Moment", "2026-07-20", "Canada", "video",
    ["youth","literacy","ethics"], "Conversation on algorithms, AI bias and why youth AI literacy matters now (listing).", author="Kubicek, I., & Medic, M.")
add("https://mila.quebec/en/news/summer-school-in-responsible-ai-and-human-rights-a-fourth-edition-that-shines-internationally",
    "Summer School in Responsible AI and Human Rights: A fourth edition that shines internationally", "Mila – Quebec Artificial Intelligence Institute", "2026-07-28", "Canada", "news",
    ["ethics","adult-education"], "Report on the fourth edition of Mila's Summer School in Responsible AI and Human Rights (listing).")
add("https://actua.ca/news-views/ai-exchange",
    "Equipping teachers for an AI world: Actua, MIT RAISE and TMU host global conference on AI literacy in K–12 education", "Actua", "2026-08-12", "Canada", "event",
    ["teachers","education-k12","literacy","stem-outreach"],
    "Announces the AI Exchange conference (Aug 17–18, 2026, TMU Toronto): workshops and discussion on responsible AI literacy for K–12 educators.")
add("https://www.digitalmoment.org/news/rbc-foundation-ai-learning-labs-youth-ai-literacy",
    "RBC Foundation backs Digital Moment's AI Learning Labs to expand AI literacy for youth across Canada", "Digital Moment", "2026-08-13", "Canada", "announcement",
    ["funding","literacy","youth","stem-outreach"],
    "$150,000 from RBC Foundation to take hands-on AI Learning Labs to four or five regions after early-2026 pilots reached 90+ youth.")
add("https://www.digitalmoment.org/news/cira-net-good-grant-ai-literacy",
    "Digital Moment receives CIRA grant for AI literacy", "Digital Moment", "2026-08-17", "Canada", "announcement",
    ["funding","literacy","education-k12","youth"], "CIRA Net Good grant to teach 600+ students (starting Grades 3–8) AI critical-thinking skills (listing).")
add("https://srinstitute.utoronto.ca/news/a-history-course-is-teaching-students-to-think-critically-about-ai",
    "From steam engines to algorithms: How a history course is teaching students to think critically about AI", "Schwartz Reisman Institute", "2026-08-17", "Canada", "news",
    ["post-secondary","literacy","creative"], "A U of T history course uses earlier technologies (steam engine, telegraph) to help students think critically about AI (listing).", author="Sasaki, C.")
add("https://www.digitalmoment.org/news/ai-literacy-is-a-whole-system-challenge",
    "AI literacy is a whole-system challenge", "Digital Moment", "2026-08-20", "Canada", "analysis",
    ["literacy","education-k12"], "Essay on how AI literacy can support learning across the education system (listing).")
add("https://www.raspberrypi.org/blog/support-for-ai-focused-qualification-young-people-england/",
    "Supporting a technical AI-focused qualification for young people in England", "Raspberry Pi Foundation", "2026-08-25", "UK", "announcement",
    ["youth","education-k12","workforce"], "The Foundation is creating a course to support young people pursuing an AI-focused qualification (listing).", author="Dowling, D.")
add("https://www.canada.ca/en/canadian-heritage/services/ai-culture-summit/what-we-heard.html",
    "What we heard at the National Summit on Artificial Intelligence and Culture", "Canadian Heritage", "2026-08-26", "Canada", "report",
    ["culture","creative","policy","indigenous","literacy"],
    "Report on Canada's first National Summit on AI and Culture (Banff, March 2026, 314 participants): copyright and transparency, Indigenous-led and sovereign AI, and AI literacy in culture.")
add("https://mila.quebec/en/news/tele-quebec-and-mila-join-forces-to-harness-ai-in-the-service-of-quebec-culture",
    "Télé-Québec and Mila join forces to harness AI in the service of Quebec culture", "Mila – Quebec Artificial Intelligence Institute", "2026-08-26", "Canada", "announcement",
    ["creative","culture"], "Partnership between public broadcaster Télé-Québec and Mila on AI for Quebec culture (listing).")
add("https://srinstitute.utoronto.ca/news/kaitlyn-regehr-appointed-inaugural-sri-global-fellow",
    "Kaitlyn Regehr appointed as inaugural SRI Global Fellow", "Schwartz Reisman Institute", "2026-08-31", "Canada", "announcement",
    ["literacy","youth","research"], "Digital-culture and AI-literacy scholar Kaitlyn Regehr will lead a large initiative on AI's impacts on children and young people.")
add("https://www.raspberrypi.org/blog/experience-ai-evolves-with-flexible-resources-for-every-classroom/",
    "Experience AI evolves with flexible resources for every classroom", "Raspberry Pi Foundation", "2026-09-07", "UK", "resource",
    ["literacy","teachers","education-k12"], "Experience AI adds flexible free AI-literacy resources for teachers (listing).", author="Garside, B.")
add("https://actua.ca/news-views/national-ai-literacy-initiative",
    "Actua welcomes federal investment in Canada's National AI Literacy Initiative", "Actua", "2026-09-10", "Canada", "statement",
    ["literacy","policy","stem-outreach"], "Actua welcomes the newly announced National AI Literacy Initiative delivered with Amii.")
add("https://srinstitute.utoronto.ca/news/u-of-t-researcher-calls-for-independent-testing-of-powerful-ai-models",
    "U of T researcher calls for independent testing of powerful AI models", "Schwartz Reisman Institute", "2026-09-10", "Canada", "opinion",
    ["safety","policy","research"], "Nicolas Papernot argues universities can act as a transparency bridge by testing new AI models for cybersecurity threats before release.", author="Bresge, A.")
add("https://dailyhive.com/canada/ai-free-course-canada",
    "Canadians can sign up for the government's free AI basics course", "Daily Hive", "2026-09-14", "Canada", "news",
    ["literacy","adult-education","teachers","post-secondary"],
    "$13M funds three free courses (teachers, post-secondary students, all Canadians); the first open to teachers and students from September 21.", author="Mountjoy, M.")
add("https://mila.quebec/en/news/mila-and-mozilla-announce-new-initiative-to-build-trustworthy-open-source-ai-for-everyone",
    "Mila and Mozilla announce new initiative to build trustworthy open source AI for everyone", "Mila – Quebec Artificial Intelligence Institute", "2026-09-17", "Canada", "announcement",
    ["research","funding","ethics","community"], "Open-source AI foundation layer organisations can run locally, with federal support; Mozilla provides $5M and Hypertec $1M, Mila leads delivery.")
add("https://www.canada.ca/en/employment-social-development/news/2026/09/government-of-canada-launches-black-canadian-communities-program.html",
    "Government of Canada launches Black Canadian Communities Program", "Employment and Social Development Canada", "2026-09-20", "Canada", "announcement",
    ["funding","black-communities","youth","community"],
    "$135.7M over five years (then $27.1M/year) for the Black Canadian Communities Program, plus $800K+ for the National Black Canadians Summit and Power of Youth Initiative.")
add("https://srinstitute.utoronto.ca/news/sri-submits-recommendations-to-federal-consultation-on-ai-transparency",
    "SRI submits recommendations to federal consultation on AI transparency", "Schwartz Reisman Institute", "2026-09-23", "Canada", "report",
    ["policy","ethics"], "Nine recommendations treating AI transparency as information infrastructure, drawing on 20 SRI-affiliated researchers.")
add("https://actua.ca/news-views/ndtr2026",
    "Statement from the CEO: National Day for Truth and Reconciliation", "Actua", "2026-09-30", "Canada", "statement",
    ["indigenous","stem-outreach"], "Actua's CEO reflects on reconciliation and Actua's work with community partners to centre Indigenous knowledge in STEM.")
add("https://www.torontomu.ca/engineering-architectural-science/stories-events/stories/2026/10/actua-partners-with-tmu-to-host-ai-conference-to-empower-educators/",
    "Actua partners with TMU to host AI conference to empower educators", "Toronto Metropolitan University", "2026-10-01", "Canada", "news",
    ["teachers","education-k12","literacy","stem-outreach"],
    "Educators from Canada, the US and Hong Kong met at TMU for the two-day AI Exchange led by Actua with MIT RAISE, building classroom AI-literacy skills.")
add("https://www.digitalmoment.org/news/op-ed-trust-not-speed-will-inevitably-be-the-measure-of-long-term-success",
    "Op-ed: Trust, not speed, will inevitably be the measure of long-term success", "Digital Moment", "2026-10-01", "Canada", "opinion",
    ["policy","literacy","community"], "Digital Moment's CEO on AI for All and why AI literacy must reach every classroom, kitchen table and community (listing).", author="Kubicek, I.")
add("https://www.amii.ca/updates-insights/how-ai-is-decoding-history-and-empowering-voices",
    "How AI is decoding history and empowering African voices", "Alberta Machine Intelligence Institute (Amii)", "2026-10-02", "Canada", "news",
    ["black-communities","culture","community"], "Amii story on AI used to decode history and amplify African voices (listing).")
add("https://uwaterloo.ca/global-engagement-seminar/events/public-talk-painted-pony-called-ai",
    "Public talk: A painted pony called AI", "University of Waterloo Global Engagement Seminar", "2026-10-06", "Canada", "event",
    ["indigenous","indigenous-futurism","community","workforce"],
    "Dr. Caroline Running Wolf uses the arrival of the horse in Indigenous communities as a metaphor for AI shaped by Indigenous leadership, community-owned language data and sovereign infrastructure.")
add("https://srinstitute.utoronto.ca/news/sri-researchers-at-4s-2026-in-toronto",
    "SRI researchers examine AI, care, and labour at 4S 2026", "Schwartz Reisman Institute", "2026-10-07", "Canada", "event",
    ["research","workforce","ethics"], "SRI researchers present in nearly 30 sessions at 4S 2026 in Toronto on AI political economy, care, labour, surveillance and data justice.")
add("https://www.gla.ac.uk/research/az/datascience/events/lovelace-hodgkinsymposium2026/",
    "Lovelace–Hodgkin Symposium 2026: Making the invisible, visible", "University of Glasgow Centre for Data Science & AI", "2026-10-13", "UK", "event",
    ["ethics","creative","community","indigenous"],
    "One-day symposium on AI's missing data, stories, power and participation through talks, workshops, games and artworks, closing with a film on mapping in Indigenous territories.")
add("https://srinstitute.utoronto.ca/news/sri-researchers-join-global-call",
    "SRI leadership and affiliates join global call for urgent AI cybersecurity safeguards", "Schwartz Reisman Institute", "2026-10-13", "Canada", "statement",
    ["safety","policy"], "400+ academics from 30+ countries sign an open letter calling for changes to how AI systems are developed, tested and deployed.")
add("https://srinstitute.utoronto.ca/news/u-of-t-led-project-pioneers-culturally-grounded-ai-for-mental-health-care-in-bangladesh",
    "Syed Ishtiaque Ahmed leads project pioneering culturally grounded AI for mental health care in Bangladesh", "Schwartz Reisman Institute", "2026-10-16", "Canada", "research",
    ["research","ethics","community"], "Project aims to close the gap between how AI models understand distress and how people experience it (listing).", author="Zucker, C.")
add("https://www.amii.ca/updates-insights/amii-and-prairiescan-expand-successful-ai-adoption-program",
    "Amii and PrairiesCan expand successful AI adoption program across the Prairies", "Alberta Machine Intelligence Institute (Amii)", "2026-10-27", "Canada", "announcement",
    ["funding","workforce"], "Federal regional agency PrairiesCan and Amii expand an AI adoption program (listing).")
add("https://www.digitalmoment.org/news/the-guiding-principles-of-digital-moments-ai-literacy-framework",
    "The guiding principles of Digital Moment's AI Literacy Framework", "Digital Moment", "2026-10-29", "Canada", "resource",
    ["literacy","teachers","education-k12"], "Framework principles arguing that sustainable AI literacy depends on shared responsibility across the education ecosystem (listing).")
add("https://www.adalovelaceinstitute.org/press-release/home-office-announcement-on-police-facial-recognition-legislation/",
    "Ada Lovelace Institute response to Home Office announcement on police facial recognition legislation", "Ada Lovelace Institute", "2026-11-04", "UK", "statement",
    ["ethics","policy","safety"], "Response to UK plans for an independent watchdog and a specific law governing police use of facial recognition.")
add("https://srinstitute.utoronto.ca/news/new-report-examines-ais-rapid-evolution-and-impact-on-society",
    "New report examines AI's rapid evolution and impact on society", "Schwartz Reisman Institute", "2026-11-10", "Canada", "report",
    ["research","ethics"], "New AI100 report; Professor Sheila McIlraith chairs the international committee guiding the century-long study of AI and society (listing).", author="Hinsta, M.")

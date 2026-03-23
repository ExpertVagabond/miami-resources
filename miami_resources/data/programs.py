"""
Real Miami-Dade County, Florida, and federal assistance programs.
All phone numbers and websites verified as of March 2026.
"""

PROGRAMS: list[dict] = [
    # ── HOUSING ──────────────────────────────────────────────
    {
        "id": "housing-section8",
        "category": "housing",
        "name": {
            "en": "Section 8 Housing Choice Voucher",
            "es": "Voucher de Elección de Vivienda Sección 8",
            "ht": "Koupon Chwa Lojman Seksyon 8",
        },
        "description": {
            "en": "Federal rental assistance that pays a portion of rent for low-income families, elderly, and disabled individuals.",
            "es": "Asistencia federal de alquiler que paga una porción del alquiler para familias de bajos ingresos, ancianos y personas con discapacidades.",
            "ht": "Asistans lwaye federal ki peye yon pòsyon lwaye pou fanmi ki gen ti revni, granmoun aje, ak moun andikape.",
        },
        "eligibility": {
            "en": "Income below 50% of area median. Priority for extremely low income (30% AMI).",
            "es": "Ingresos por debajo del 50% de la mediana del área. Prioridad para ingresos extremadamente bajos (30% AMI).",
            "ht": "Revni anba 50% medyàn zòn nan. Priyorite pou revni ekstrèmman ba (30% AMI).",
        },
        "phone": "786-469-4100",
        "website": "https://www.miamidade.gov/global/housing/home.page",
        "address": "701 NW 1st Court, Miami, FL 33136",
        "level": "federal",
    },
    {
        "id": "housing-public",
        "category": "housing",
        "name": {
            "en": "Miami-Dade Public Housing",
            "es": "Vivienda Pública de Miami-Dade",
            "ht": "Lojman Piblik Miami-Dade",
        },
        "description": {
            "en": "Affordable housing units owned and managed by Miami-Dade County for low-income residents.",
            "es": "Unidades de vivienda asequible administradas por el condado de Miami-Dade para residentes de bajos ingresos.",
            "ht": "Inite lojman abòdab ke Konte Miami-Dade jere pou rezidan ki gen ti revni.",
        },
        "eligibility": {
            "en": "Income limits vary by family size. Must be a legal resident.",
            "es": "Límites de ingresos varían según el tamaño de la familia. Debe ser residente legal.",
            "ht": "Limit revni varye selon gwosè fanmi. Dwe yon rezidan legal.",
        },
        "phone": "786-469-4100",
        "website": "https://www.miamidade.gov/global/housing/public-housing.page",
        "address": "701 NW 1st Court, Miami, FL 33136",
        "level": "county",
    },
    {
        "id": "housing-ship",
        "category": "housing",
        "name": {
            "en": "SHIP — State Housing Initiatives Partnership",
            "es": "SHIP — Programa Estatal de Iniciativas de Vivienda",
            "ht": "SHIP — Pwogram Inisyativ Lojman Eta a",
        },
        "description": {
            "en": "Florida state program providing down payment assistance, rehab funds, and emergency home repairs.",
            "es": "Programa estatal de Florida que ofrece asistencia para el pago inicial, fondos de rehabilitación y reparaciones de emergencia.",
            "ht": "Pwogram eta Florid ki bay asistans pou premye peman, fon reyabilitasyon, ak reparasyon ijans kay.",
        },
        "eligibility": {
            "en": "Income at or below 120% AMI. Must be a Florida resident.",
            "es": "Ingresos iguales o inferiores al 120% AMI. Debe ser residente de Florida.",
            "ht": "Revni egal oswa anba 120% AMI. Dwe yon rezidan Florid.",
        },
        "phone": "786-469-4100",
        "website": "https://www.floridahousing.org/programs/ship",
        "address": "701 NW 1st Court, Miami, FL 33136",
        "level": "state",
    },
    {
        "id": "housing-era",
        "category": "housing",
        "name": {
            "en": "Emergency Rental Assistance",
            "es": "Asistencia de Alquiler de Emergencia",
            "ht": "Asistans Lwaye Ijans",
        },
        "description": {
            "en": "Emergency funds for tenants behind on rent or facing eviction. Covers rent and utility arrears.",
            "es": "Fondos de emergencia para inquilinos atrasados en el alquiler o que enfrentan desalojo.",
            "ht": "Fon ijans pou lokatè ki an reta nan lwaye oswa ki fè fas ak degèpisman.",
        },
        "eligibility": {
            "en": "Must demonstrate financial hardship. Income below 80% AMI.",
            "es": "Debe demostrar dificultades financieras. Ingresos por debajo del 80% AMI.",
            "ht": "Dwe demontre difikilte finansyè. Revni anba 80% AMI.",
        },
        "phone": "305-358-4357",
        "website": "https://www.miamidade.gov/global/housing/emergency-rental-assistance.page",
        "address": "111 NW 1st Street, Miami, FL 33128",
        "level": "county",
    },
    {
        "id": "housing-habitat",
        "category": "housing",
        "name": {
            "en": "Habitat for Humanity Greater Miami",
            "es": "Hábitat para la Humanidad del Gran Miami",
            "ht": "Habitat pou Limanite Greater Miami",
        },
        "description": {
            "en": "Builds and repairs affordable homes. Homeownership program with 0% interest mortgages.",
            "es": "Construye y repara viviendas asequibles. Programa de propiedad con hipotecas al 0% de interés.",
            "ht": "Bati ak repare kay abòdab. Pwogram pwopriyetè kay ak ipotèk 0% enterè.",
        },
        "eligibility": {
            "en": "Income between 30-80% AMI. Willing to partner (sweat equity hours).",
            "es": "Ingresos entre 30-80% AMI. Dispuesto a participar (horas de trabajo voluntario).",
            "ht": "Revni ant 30-80% AMI. Vle patisipe (èdtan travay volontè).",
        },
        "phone": "305-634-3628",
        "website": "https://miamihabitat.org",
        "address": "3800 NW 22nd Avenue, Miami, FL 33142",
        "level": "nonprofit",
    },
    {
        "id": "housing-homeless-trust",
        "category": "housing",
        "name": {
            "en": "Miami-Dade Homeless Trust",
            "es": "Fideicomiso para Personas sin Hogar de Miami-Dade",
            "ht": "Trust Sanzabri Miami-Dade",
        },
        "description": {
            "en": "Coordinates the county's homeless continuum of care: shelters, transitional housing, and permanent supportive housing.",
            "es": "Coordina el sistema de atención a personas sin hogar del condado: refugios, vivienda de transición y vivienda permanente de apoyo.",
            "ht": "Kowòdone sistèm swen sanzabri konte a: abri, lojman tranzisyon, ak lojman pèmanan ak sipò.",
        },
        "eligibility": {
            "en": "Individuals and families experiencing homelessness. Call for intake assessment.",
            "es": "Personas y familias sin hogar. Llame para evaluación de admisión.",
            "ht": "Moun ak fanmi ki sanzabri. Rele pou evalyasyon admisyon.",
        },
        "phone": "786-469-4800",
        "website": "https://www.homelesstrust.org",
        "address": "111 NW 1st Street, Suite 27-310, Miami, FL 33128",
        "level": "county",
    },
    {
        "id": "housing-camillus",
        "category": "housing",
        "name": {
            "en": "Camillus House",
            "es": "Camillus House",
            "ht": "Camillus House",
        },
        "description": {
            "en": "Comprehensive services for homeless individuals: emergency shelter, meals, health clinic, job training, and permanent housing.",
            "es": "Servicios integrales para personas sin hogar: refugio de emergencia, comidas, clínica de salud, capacitación laboral y vivienda permanente.",
            "ht": "Sèvis konplè pou moun sanzabri: abri ijans, manje, klinik sante, fòmasyon travay, ak lojman pèmanan.",
        },
        "eligibility": {
            "en": "Open to all individuals experiencing homelessness. Walk-ins accepted.",
            "es": "Abierto a todas las personas sin hogar. Se aceptan visitas sin cita.",
            "ht": "Louvri pou tout moun ki sanzabri. Aksepte san randevou.",
        },
        "phone": "305-374-1065",
        "website": "https://www.camillushouse.org",
        "address": "1603 NW 7th Avenue, Miami, FL 33136",
        "level": "nonprofit",
    },
    # ── FOOD ─────────────────────────────────────────────────
    {
        "id": "food-snap",
        "category": "food",
        "name": {
            "en": "SNAP (Food Stamps)",
            "es": "SNAP (Cupones de Alimentos)",
            "ht": "SNAP (Koupon Manje)",
        },
        "description": {
            "en": "Federal nutrition program providing monthly benefits on an EBT card to buy groceries.",
            "es": "Programa federal de nutrición que proporciona beneficios mensuales en una tarjeta EBT para comprar alimentos.",
            "ht": "Pwogram nitrisyon federal ki bay benefis chak mwa sou yon kat EBT pou achte manje.",
        },
        "eligibility": {
            "en": "Gross income below 200% FPL for most households. Apply online at MyACCESS.",
            "es": "Ingreso bruto por debajo del 200% del nivel federal de pobreza. Solicite en línea en MyACCESS.",
            "ht": "Revni brit anba 200% FPL pou pifò kay. Aplike sou entènèt nan MyACCESS.",
        },
        "phone": "866-762-2237",
        "website": "https://www.myflfamilies.com/services/public-assistance/food-assistance",
        "address": "Apply online or visit any Florida DCF service center",
        "level": "federal",
    },
    {
        "id": "food-wic",
        "category": "food",
        "name": {
            "en": "WIC — Women, Infants & Children",
            "es": "WIC — Mujeres, Bebés y Niños",
            "ht": "WIC — Fanm, Tibebe ak Timoun",
        },
        "description": {
            "en": "Nutrition program for pregnant/postpartum women, infants, and children under 5. Provides food packages, nutrition education, and healthcare referrals.",
            "es": "Programa de nutrición para mujeres embarazadas/posparto, bebés y niños menores de 5 años. Proporciona paquetes de alimentos, educación nutricional y referencias médicas.",
            "ht": "Pwogram nitrisyon pou fanm ansent/apre akouchman, tibebe, ak timoun anba 5 an. Bay pake manje, edikasyon nitrisyon, ak referans medikal.",
        },
        "eligibility": {
            "en": "Pregnant women, new mothers, infants, children under 5. Income below 185% FPL.",
            "es": "Mujeres embarazadas, nuevas madres, bebés, niños menores de 5 años. Ingresos por debajo del 185% FPL.",
            "ht": "Fanm ansent, nouvo manman, tibebe, timoun anba 5 an. Revni anba 185% FPL.",
        },
        "phone": "800-342-3556",
        "website": "https://www.floridahealth.gov/programs-and-services/wic/",
        "address": "Multiple WIC offices across Miami-Dade",
        "level": "federal",
    },
    {
        "id": "food-feeding-south-fl",
        "category": "food",
        "name": {
            "en": "Feeding South Florida",
            "es": "Alimentando el Sur de Florida",
            "ht": "Nouri Sid Florid",
        },
        "description": {
            "en": "Largest food bank in South Florida. Distributes food through 500+ partner agencies. Find a pantry near you on their website.",
            "es": "El banco de alimentos más grande del sur de Florida. Distribuye alimentos a través de más de 500 agencias asociadas.",
            "ht": "Pi gwo bank manje nan Sid Florid. Distribye manje atravè plis pase 500 ajans patnè.",
        },
        "eligibility": {
            "en": "Open to anyone in need. No ID or proof of income required at most distribution sites.",
            "es": "Abierto a cualquier persona necesitada. No se requiere identificación ni prueba de ingresos en la mayoría de los sitios.",
            "ht": "Louvri pou nenpòt moun ki bezwen. Pa bezwen ID oswa prèv revni nan pifò sit distribisyon.",
        },
        "phone": "954-518-1818",
        "website": "https://feedingsouthflorida.org",
        "address": "2501 SW 32nd Terrace, Pembroke Park, FL 33023",
        "level": "nonprofit",
    },
    {
        "id": "food-farm-share",
        "category": "food",
        "name": {
            "en": "Farm Share",
            "es": "Farm Share",
            "ht": "Farm Share",
        },
        "description": {
            "en": "Fresh produce distribution to low-income communities. Weekly distributions at sites across Miami-Dade.",
            "es": "Distribución de productos frescos a comunidades de bajos ingresos. Distribuciones semanales en sitios de Miami-Dade.",
            "ht": "Distribisyon pwodui fre bay kominote ki gen ti revni. Distribisyon chak semèn nan sit atravè Miami-Dade.",
        },
        "eligibility": {
            "en": "Open to anyone. First come, first served at distribution events.",
            "es": "Abierto a todos. Primer llegado, primer servido en los eventos de distribución.",
            "ht": "Louvri pou tout moun. Premye rive, premye sèvi nan evènman distribisyon.",
        },
        "phone": "305-246-3276",
        "website": "https://farmshare.org",
        "address": "12550 SW 216th Street, Goulds, FL 33170",
        "level": "nonprofit",
    },
    {
        "id": "food-daily-bread",
        "category": "food",
        "name": {
            "en": "Daily Bread Food Bank",
            "es": "Banco de Alimentos Daily Bread",
            "ht": "Bank Manje Daily Bread",
        },
        "description": {
            "en": "Provides groceries and hot meals in the Overtown area and beyond. Walk-in pantry and meal service.",
            "es": "Proporciona comestibles y comidas calientes en el área de Overtown y más allá.",
            "ht": "Bay pwovizyon ak manje cho nan zòn Overtown ak pi lwen.",
        },
        "eligibility": {
            "en": "Open to anyone in need. Overtown residents prioritized.",
            "es": "Abierto a cualquier persona necesitada. Residentes de Overtown tienen prioridad.",
            "ht": "Louvri pou nenpòt moun ki bezwen. Rezidan Overtown gen priyorite.",
        },
        "phone": "305-635-5700",
        "website": "https://dailybreadfoodbank.org",
        "address": "2975 NW 12th Avenue, Miami, FL 33127",
        "level": "nonprofit",
    },
    {
        "id": "food-school-meals",
        "category": "food",
        "name": {
            "en": "Free School Meals — Miami-Dade County Public Schools",
            "es": "Comidas Escolares Gratuitas — Escuelas Públicas de Miami-Dade",
            "ht": "Manje Lekòl Gratis — Lekòl Piblik Konte Miami-Dade",
        },
        "description": {
            "en": "All Miami-Dade public school students receive free breakfast and lunch through the Community Eligibility Provision.",
            "es": "Todos los estudiantes de escuelas públicas de Miami-Dade reciben desayuno y almuerzo gratis.",
            "ht": "Tout elèv lekòl piblik Miami-Dade resevwa dejene ak manje midi gratis.",
        },
        "eligibility": {
            "en": "All enrolled Miami-Dade public school students. No application needed.",
            "es": "Todos los estudiantes inscritos en escuelas públicas de Miami-Dade. No se necesita solicitud.",
            "ht": "Tout elèv ki enskri nan lekòl piblik Miami-Dade. Pa bezwen aplikasyon.",
        },
        "phone": "305-995-1000",
        "website": "https://www.dadeschools.net/food",
        "address": "All Miami-Dade public schools",
        "level": "county",
    },
    {
        "id": "food-meals-on-wheels",
        "category": "food",
        "name": {
            "en": "Meals on Wheels — Alliance for Aging",
            "es": "Meals on Wheels — Alianza para el Envejecimiento",
            "ht": "Meals on Wheels — Alyans pou Granmoun Aje",
        },
        "description": {
            "en": "Home-delivered meals for seniors 60+ who are homebound or have difficulty preparing food.",
            "es": "Comidas entregadas a domicilio para personas mayores de 60 años que están confinadas en casa.",
            "ht": "Manje livre lakay pou granmoun aje 60+ ki pa ka sòti oswa ki gen difikilte pou prepare manje.",
        },
        "eligibility": {
            "en": "Adults 60 and older. Priority for homebound, living alone, or with disabilities.",
            "es": "Adultos de 60 años o más. Prioridad para personas confinadas en casa, que viven solas o con discapacidades.",
            "ht": "Granmoun 60 an oswa plis. Priyorite pou moun ki pa ka sòti, ki viv pou kont yo, oswa ki gen andikap.",
        },
        "phone": "305-670-6500",
        "website": "https://www.allianceforaging.org",
        "address": "760 NW 107th Avenue, Suite 214, Miami, FL 33172",
        "level": "county",
    },
    # ── HEALTHCARE ───────────────────────────────────────────
    {
        "id": "health-jackson",
        "category": "healthcare",
        "name": {
            "en": "Jackson Health System",
            "es": "Sistema de Salud Jackson",
            "ht": "Sistèm Sante Jackson",
        },
        "description": {
            "en": "Miami-Dade's public hospital system. Provides care regardless of ability to pay. Includes Jackson Memorial, emergency rooms, and community clinics.",
            "es": "Sistema hospitalario público de Miami-Dade. Brinda atención sin importar la capacidad de pago.",
            "ht": "Sistèm lopital piblik Miami-Dade. Bay swen kèlkeswa kapasite pou peye.",
        },
        "eligibility": {
            "en": "Open to all. Financial assistance (Jackson Plan) available for uninsured Miami-Dade residents.",
            "es": "Abierto a todos. Asistencia financiera (Plan Jackson) disponible para residentes sin seguro.",
            "ht": "Louvri pou tout moun. Asistans finansyè (Plan Jackson) disponib pou rezidan ki pa gen asirans.",
        },
        "phone": "305-585-1111",
        "website": "https://jacksonhealth.org",
        "address": "1611 NW 12th Avenue, Miami, FL 33136",
        "level": "county",
    },
    {
        "id": "health-chi",
        "category": "healthcare",
        "name": {
            "en": "Community Health of South Florida (CHI)",
            "es": "Salud Comunitaria del Sur de Florida (CHI)",
            "ht": "Sante Kominotè Sid Florid (CHI)",
        },
        "description": {
            "en": "Federally Qualified Health Center providing primary care, dental, behavioral health, and pharmacy on a sliding fee scale.",
            "es": "Centro de salud con calificación federal que ofrece atención primaria, dental, salud mental y farmacia con escala de tarifas ajustables.",
            "ht": "Sant sante ki kalifye federalman ki bay swen primè, dantè, sante mantal, ak famasi sou yon echèl frè ajistab.",
        },
        "eligibility": {
            "en": "Open to all. Sliding fee scale based on income. No one turned away.",
            "es": "Abierto a todos. Escala de tarifas según ingresos. Nadie es rechazado.",
            "ht": "Louvri pou tout moun. Echèl frè baze sou revni. Yo pa refize pèsonn.",
        },
        "phone": "305-252-4820",
        "website": "https://chisouthfl.org",
        "address": "10300 SW 216th Street, Miami, FL 33190",
        "level": "federal",
    },
    {
        "id": "health-medicaid",
        "category": "healthcare",
        "name": {
            "en": "Florida Medicaid",
            "es": "Medicaid de Florida",
            "ht": "Florida Medicaid",
        },
        "description": {
            "en": "Free or low-cost health coverage for low-income families, children, pregnant women, elderly, and disabled individuals.",
            "es": "Cobertura médica gratuita o de bajo costo para familias de bajos ingresos, niños, mujeres embarazadas, ancianos y personas con discapacidades.",
            "ht": "Asirans sante gratis oswa ba pri pou fanmi ki gen ti revni, timoun, fanm ansent, granmoun aje, ak moun andikape.",
        },
        "eligibility": {
            "en": "Income limits vary by category. Children, pregnant women, parents, elderly, and disabled may qualify. Apply via MyACCESS.",
            "es": "Límites de ingresos varían por categoría. Niños, embarazadas, padres, ancianos y discapacitados pueden calificar. Solicite en MyACCESS.",
            "ht": "Limit revni varye selon kategori. Timoun, fanm ansent, paran, granmoun aje, ak moun andikape ka kalifye. Aplike nan MyACCESS.",
        },
        "phone": "877-711-3662",
        "website": "https://www.myflfamilies.com/services/public-assistance/medicaid",
        "address": "Apply online at MyACCESS or visit any DCF service center",
        "level": "federal",
    },
    {
        "id": "health-kidcare",
        "category": "healthcare",
        "name": {
            "en": "Florida KidCare",
            "es": "Florida KidCare",
            "ht": "Florida KidCare",
        },
        "description": {
            "en": "Affordable health insurance for children under 19. Includes Medicaid, MediKids, Florida Healthy Kids, and CMS.",
            "es": "Seguro médico asequible para niños menores de 19 años. Incluye Medicaid, MediKids, Florida Healthy Kids y CMS.",
            "ht": "Asirans sante abòdab pou timoun anba 19 an. Gen ladan Medicaid, MediKids, Florida Healthy Kids, ak CMS.",
        },
        "eligibility": {
            "en": "Uninsured children under 19. Family income up to 400% FPL depending on the program.",
            "es": "Niños sin seguro menores de 19 años. Ingresos familiares hasta 400% FPL según el programa.",
            "ht": "Timoun san asirans anba 19 an. Revni fanmi jiska 400% FPL selon pwogram nan.",
        },
        "phone": "888-540-5437",
        "website": "https://www.floridakidcare.org",
        "address": "Apply online or call for assistance",
        "level": "state",
    },
    {
        "id": "health-borinquen",
        "category": "healthcare",
        "name": {
            "en": "Borinquen Health Care Center",
            "es": "Centro de Salud Borinquen",
            "ht": "Sant Sante Borinquen",
        },
        "description": {
            "en": "FQHC serving Little Havana and surrounding areas. Primary care, dental, OB/GYN, pediatrics, mental health, and pharmacy.",
            "es": "Centro de salud que sirve a Little Havana y áreas circundantes. Atención primaria, dental, obstetricia, pediatría, salud mental y farmacia.",
            "ht": "Sant sante ki sèvi Little Havana ak zòn ki anviwone. Swen primè, dantè, obstetrik, pedyatri, sante mantal, ak famasi.",
        },
        "eligibility": {
            "en": "Open to all. Sliding fee scale. Accepts Medicaid, Medicare, and most insurance.",
            "es": "Abierto a todos. Escala de tarifas ajustables. Acepta Medicaid, Medicare y la mayoría de seguros.",
            "ht": "Louvri pou tout moun. Echèl frè ajistab. Aksepte Medicaid, Medicare, ak pifò asirans.",
        },
        "phone": "305-576-6611",
        "website": "https://borinquenhealth.org",
        "address": "3601 Federal Highway, Miami, FL 33137",
        "level": "federal",
    },
    {
        "id": "health-jessie-trice",
        "category": "healthcare",
        "name": {
            "en": "Jessie Trice Community Health System",
            "es": "Sistema de Salud Comunitaria Jessie Trice",
            "ht": "Sistèm Sante Kominotè Jessie Trice",
        },
        "description": {
            "en": "FQHC specializing in care for underserved communities in Liberty City, Opa-locka, and surrounding areas.",
            "es": "Centro de salud especializado en atención a comunidades desatendidas en Liberty City, Opa-locka y áreas cercanas.",
            "ht": "Sant sante ki espesyalize nan swen pou kominote ki pa gen ase sèvis nan Liberty City, Opa-locka, ak zòn ki anviwone.",
        },
        "eligibility": {
            "en": "Open to all. Sliding fee scale based on income.",
            "es": "Abierto a todos. Escala de tarifas según ingresos.",
            "ht": "Louvri pou tout moun. Echèl frè baze sou revni.",
        },
        "phone": "305-637-6400",
        "website": "https://jessietrice.org",
        "address": "5607 NW 27th Avenue, Miami, FL 33142",
        "level": "federal",
    },
    {
        "id": "health-mental-jackson",
        "category": "healthcare",
        "name": {
            "en": "Jackson Behavioral Health Hospital",
            "es": "Hospital de Salud Mental Jackson",
            "ht": "Lopital Sante Mantal Jackson",
        },
        "description": {
            "en": "Psychiatric emergency services, inpatient and outpatient mental health care, substance abuse treatment.",
            "es": "Servicios psiquiátricos de emergencia, atención de salud mental ambulatoria y hospitalaria, tratamiento de abuso de sustancias.",
            "ht": "Sèvis ijans sikyatrik, swen sante mantal andedan ak deyò lopital, tretman abi sibstans.",
        },
        "eligibility": {
            "en": "Open to all. Walk-in crisis stabilization available 24/7.",
            "es": "Abierto a todos. Estabilización de crisis sin cita disponible 24/7.",
            "ht": "Louvri pou tout moun. Estabilizasyon kriz san randevou disponib 24/7.",
        },
        "phone": "305-355-7000",
        "website": "https://jacksonhealth.org/jackson-behavioral-health-hospital/",
        "address": "1695 NW 9th Avenue, Miami, FL 33136",
        "level": "county",
    },
    # ── JOBS ─────────────────────────────────────────────────
    {
        "id": "jobs-careersource",
        "category": "jobs",
        "name": {
            "en": "CareerSource South Florida",
            "es": "CareerSource Sur de Florida",
            "ht": "CareerSource Sid Florid",
        },
        "description": {
            "en": "Free career services: job search, resume help, interview prep, skills training, and hiring events. Multiple locations.",
            "es": "Servicios de carrera gratuitos: búsqueda de empleo, ayuda con currículum, preparación para entrevistas, capacitación y ferias de empleo.",
            "ht": "Sèvis karyè gratis: rechèch travay, èd ak CV, preparasyon pou entèvyou, fòmasyon ladrès, ak evènman anbochaj.",
        },
        "eligibility": {
            "en": "Open to all job seekers and employers in Miami-Dade and Monroe counties.",
            "es": "Abierto a todos los buscadores de empleo y empleadores en los condados de Miami-Dade y Monroe.",
            "ht": "Louvri pou tout moun k ap chèche travay ak anplwayè nan konte Miami-Dade ak Monroe.",
        },
        "phone": "305-594-7615",
        "website": "https://careersourcesfl.com",
        "address": "7300 Corporate Center Drive, Suite 500, Miami, FL 33126",
        "level": "state",
    },
    {
        "id": "jobs-employ-miami-dade",
        "category": "jobs",
        "name": {
            "en": "Employ Miami-Dade",
            "es": "Employ Miami-Dade",
            "ht": "Employ Miami-Dade",
        },
        "description": {
            "en": "County-run employment program connecting residents to local jobs, internships, and apprenticeships.",
            "es": "Programa de empleo del condado que conecta residentes con empleos locales, pasantías y aprendizajes.",
            "ht": "Pwogram travay konte a ki konekte rezidan ak travay lokal, estaj, ak aprantisaj.",
        },
        "eligibility": {
            "en": "Miami-Dade County residents. Priority for youth, veterans, and formerly incarcerated.",
            "es": "Residentes del condado de Miami-Dade. Prioridad para jóvenes, veteranos y personas con antecedentes penales.",
            "ht": "Rezidan Konte Miami-Dade. Priyorite pou jèn, veteran, ak moun ki te nan prizon.",
        },
        "phone": "305-375-5665",
        "website": "https://www8.miamidade.gov/global/economy/employ-miami-dade.page",
        "address": "111 NW 1st Street, Miami, FL 33128",
        "level": "county",
    },
    {
        "id": "jobs-goodwill",
        "category": "jobs",
        "name": {
            "en": "Goodwill Industries of South Florida",
            "es": "Goodwill Industries del Sur de Florida",
            "ht": "Goodwill Industries Sid Florid",
        },
        "description": {
            "en": "Job training, placement services, and career coaching. Specializes in helping people with barriers to employment.",
            "es": "Capacitación laboral, servicios de colocación y coaching de carrera. Especializado en ayudar a personas con barreras para el empleo.",
            "ht": "Fòmasyon travay, sèvis plasman, ak coaching karyè. Espesyalize nan ede moun ki gen baryè pou travay.",
        },
        "eligibility": {
            "en": "Open to all. Focus on individuals facing barriers: disabilities, criminal records, limited education.",
            "es": "Abierto a todos. Enfoque en personas con barreras: discapacidades, antecedentes penales, educación limitada.",
            "ht": "Louvri pou tout moun. Konsantre sou moun ki gen baryè: andikap, dosye kriminèl, edikasyon limite.",
        },
        "phone": "305-325-9114",
        "website": "https://goodwillsouthflorida.org",
        "address": "2121 NW 21st Street, Miami, FL 33142",
        "level": "nonprofit",
    },
    {
        "id": "jobs-catalyst",
        "category": "jobs",
        "name": {
            "en": "Catalyst Miami",
            "es": "Catalyst Miami",
            "ht": "Catalyst Miami",
        },
        "description": {
            "en": "Financial coaching, workforce development, and community leadership training. Helps families build economic stability.",
            "es": "Coaching financiero, desarrollo laboral y capacitación en liderazgo comunitario. Ayuda a familias a construir estabilidad económica.",
            "ht": "Coaching finansyè, devlopman mendèv, ak fòmasyon lidèchip kominotè. Ede fanmi bati estabilite ekonomik.",
        },
        "eligibility": {
            "en": "Low-to-moderate income Miami-Dade residents.",
            "es": "Residentes de Miami-Dade con ingresos bajos a moderados.",
            "ht": "Rezidan Miami-Dade ki gen revni ba a modere.",
        },
        "phone": "305-576-5001",
        "website": "https://catalystmiami.org",
        "address": "3025 Brickell Avenue, Miami, FL 33129",
        "level": "nonprofit",
    },
    {
        "id": "jobs-ser",
        "category": "jobs",
        "name": {
            "en": "SER Jobs for Progress National",
            "es": "SER Jobs for Progress National",
            "ht": "SER Jobs for Progress National",
        },
        "description": {
            "en": "Employment and training for the Hispanic community and other underserved populations. GED prep, ESL, vocational training.",
            "es": "Empleo y capacitación para la comunidad hispana y otras poblaciones desatendidas. Preparación para GED, ESL, capacitación vocacional.",
            "ht": "Travay ak fòmasyon pou kominote Panyòl ak lòt popilasyon ki pa gen ase sèvis. Preparasyon GED, ESL, fòmasyon vokasyonèl.",
        },
        "eligibility": {
            "en": "Open to all. Focus on Hispanic and underserved communities.",
            "es": "Abierto a todos. Enfoque en comunidades hispanas y desatendidas.",
            "ht": "Louvri pou tout moun. Konsantre sou kominote Panyòl ak kominote ki pa gen ase sèvis.",
        },
        "phone": "305-643-4419",
        "website": "https://ser-national.org",
        "address": "11 NW 36th Street, Miami, FL 33127",
        "level": "nonprofit",
    },
    {
        "id": "jobs-urban-league",
        "category": "jobs",
        "name": {
            "en": "Urban League of Greater Miami",
            "es": "Liga Urbana del Gran Miami",
            "ht": "Urban League Greater Miami",
        },
        "description": {
            "en": "Workforce development, career readiness, and small business support for Black and underserved communities.",
            "es": "Desarrollo laboral, preparación profesional y apoyo a pequeños negocios para comunidades afroamericanas y desatendidas.",
            "ht": "Devlopman mendèv, preparasyon karyè, ak sipò ti biznis pou kominote Nwa ak kominote ki pa gen ase sèvis.",
        },
        "eligibility": {
            "en": "Open to all Miami-Dade residents seeking employment or business support.",
            "es": "Abierto a todos los residentes de Miami-Dade que buscan empleo o apoyo empresarial.",
            "ht": "Louvri pou tout rezidan Miami-Dade k ap chèche travay oswa sipò biznis.",
        },
        "phone": "305-696-4450",
        "website": "https://ulm.org",
        "address": "8500 NW 25th Avenue, Miami, FL 33147",
        "level": "nonprofit",
    },
    {
        "id": "jobs-florida-deo",
        "category": "jobs",
        "name": {
            "en": "Florida Department of Economic Opportunity",
            "es": "Departamento de Oportunidad Económica de Florida",
            "ht": "Depatman Opòtinite Ekonomik Florid",
        },
        "description": {
            "en": "State job board (Employ Florida), unemployment benefits, and reemployment assistance.",
            "es": "Bolsa de trabajo estatal (Employ Florida), beneficios de desempleo y asistencia de reempleo.",
            "ht": "Tab travay eta (Employ Florida), benefis chomaj, ak asistans re-anplwa.",
        },
        "eligibility": {
            "en": "Florida residents. Unemployment benefits require prior work history.",
            "es": "Residentes de Florida. Beneficios de desempleo requieren historial laboral previo.",
            "ht": "Rezidan Florid. Benefis chomaj mande istwa travay anvan.",
        },
        "phone": "800-204-2418",
        "website": "https://floridajobs.org",
        "address": "Apply online at Employ Florida",
        "level": "state",
    },
    # ── EDUCATION ────────────────────────────────────────────
    {
        "id": "edu-mdcps",
        "category": "education",
        "name": {
            "en": "Miami-Dade County Public Schools",
            "es": "Escuelas Públicas del Condado de Miami-Dade",
            "ht": "Lekòl Piblik Konte Miami-Dade",
        },
        "description": {
            "en": "4th largest school district in the US. Free K-12 education, magnet programs, career academies, and bilingual education.",
            "es": "4to distrito escolar más grande de EE.UU. Educación gratuita K-12, programas magnet, academias profesionales y educación bilingüe.",
            "ht": "4yèm pi gwo distri lekòl nan Etazini. Edikasyon gratis K-12, pwogram magnè, akademi karyè, ak edikasyon bileng.",
        },
        "eligibility": {
            "en": "All children ages 5-18 residing in Miami-Dade County. Enrollment open year-round.",
            "es": "Todos los niños de 5-18 años que residen en el condado de Miami-Dade. Inscripción abierta todo el año.",
            "ht": "Tout timoun 5-18 an ki rete nan Konte Miami-Dade. Enskripsyon ouvè tout ane a.",
        },
        "phone": "305-995-1000",
        "website": "https://www.dadeschools.net",
        "address": "1450 NE 2nd Avenue, Miami, FL 33132",
        "level": "county",
    },
    {
        "id": "edu-mdc",
        "category": "education",
        "name": {
            "en": "Miami Dade College",
            "es": "Miami Dade College",
            "ht": "Miami Dade College",
        },
        "description": {
            "en": "Largest college in the US by enrollment. Associates degrees, bachelors, workforce certificates. 8 campuses across Miami-Dade.",
            "es": "La universidad más grande de EE.UU. por inscripción. Títulos de asociado, licenciatura, certificados laborales. 8 campus en Miami-Dade.",
            "ht": "Pi gwo kolèj nan Etazini pa enskripsyon. Diplòm asosye, bakaloreya, sètifika mendèv. 8 kanpis nan Miami-Dade.",
        },
        "eligibility": {
            "en": "Open admissions. Financial aid, Pell Grants, and scholarships available.",
            "es": "Admisión abierta. Ayuda financiera, becas Pell y becas disponibles.",
            "ht": "Admisyon ouvè. Èd finansyè, Bous Pell, ak bous disponib.",
        },
        "phone": "305-237-8888",
        "website": "https://www.mdc.edu",
        "address": "300 NE 2nd Avenue, Miami, FL 33132",
        "level": "county",
    },
    {
        "id": "edu-adult-ed",
        "category": "education",
        "name": {
            "en": "Adult Education & GED — Miami-Dade",
            "es": "Educación para Adultos y GED — Miami-Dade",
            "ht": "Edikasyon Adilt ak GED — Miami-Dade",
        },
        "description": {
            "en": "Free GED preparation, adult basic education, ESOL (English for Speakers of Other Languages), and citizenship classes.",
            "es": "Preparación gratuita para GED, educación básica para adultos, ESOL (inglés para hablantes de otros idiomas) y clases de ciudadanía.",
            "ht": "Preparasyon GED gratis, edikasyon debaz pou granmoun, ESOL (Angle pou moun ki pale lòt lang), ak klas sitwayènte.",
        },
        "eligibility": {
            "en": "Adults 16+ not enrolled in K-12. Free for Miami-Dade residents.",
            "es": "Adultos de 16+ no inscritos en K-12. Gratis para residentes de Miami-Dade.",
            "ht": "Granmoun 16+ ki pa enskri nan K-12. Gratis pou rezidan Miami-Dade.",
        },
        "phone": "305-558-8000",
        "website": "https://adulted.dadeschools.net",
        "address": "Multiple locations across Miami-Dade",
        "level": "county",
    },
    {
        "id": "edu-head-start",
        "category": "education",
        "name": {
            "en": "Head Start / Early Head Start",
            "es": "Head Start / Early Head Start",
            "ht": "Head Start / Early Head Start",
        },
        "description": {
            "en": "Free early childhood education for low-income families. Children birth to 5 years. Includes meals, health screenings, and parent support.",
            "es": "Educación infantil gratuita para familias de bajos ingresos. Niños desde el nacimiento hasta 5 años. Incluye comidas, exámenes de salud y apoyo a padres.",
            "ht": "Edikasyon timoun piti gratis pou fanmi ki gen ti revni. Timoun depi nesans jiska 5 an. Gen ladan manje, egzamen sante, ak sipò paran.",
        },
        "eligibility": {
            "en": "Families at or below 100% FPL. Children birth to 5 years. Pregnant women also eligible.",
            "es": "Familias con ingresos iguales o inferiores al 100% FPL. Niños desde el nacimiento hasta 5 años. Mujeres embarazadas también son elegibles.",
            "ht": "Fanmi ki gen revni egal oswa anba 100% FPL. Timoun depi nesans jiska 5 an. Fanm ansent kalifye tou.",
        },
        "phone": "786-336-1400",
        "website": "https://www.miamidade.gov/global/socialservices/head-start.page",
        "address": "Multiple centers across Miami-Dade",
        "level": "federal",
    },
    {
        "id": "edu-bright-futures",
        "category": "education",
        "name": {
            "en": "Florida Bright Futures Scholarship",
            "es": "Beca Florida Bright Futures",
            "ht": "Bous Florida Bright Futures",
        },
        "description": {
            "en": "Merit-based state scholarship covering tuition and fees at Florida public colleges and universities. Three award levels.",
            "es": "Beca estatal basada en mérito que cubre matrícula y tarifas en universidades públicas de Florida. Tres niveles de premio.",
            "ht": "Bous eta ki baze sou merit ki kouvri ekolaj ak frè nan kolèj ak inivèsite piblik Florid. Twa nivo prim.",
        },
        "eligibility": {
            "en": "Florida high school graduates with qualifying GPA and test scores. Must complete community service hours.",
            "es": "Graduados de secundaria de Florida con GPA y puntajes de examen calificados. Deben completar horas de servicio comunitario.",
            "ht": "Gradye lekòl segondè Florid ki gen GPA ak nòt egzamen ki kalifye. Dwe konplete èdtan sèvis kominotè.",
        },
        "phone": "888-827-2004",
        "website": "https://www.floridastudentfinancialaidsg.org/SAPHome/SAPHome?url=home",
        "address": "Apply through FAFSA and Florida Financial Aid Application",
        "level": "state",
    },
    {
        "id": "edu-pell-grant",
        "category": "education",
        "name": {
            "en": "Federal Pell Grant",
            "es": "Beca Federal Pell",
            "ht": "Bous Federal Pell",
        },
        "description": {
            "en": "Federal grant for undergraduate students with financial need. Does not need to be repaid. Up to $7,395 per year.",
            "es": "Beca federal para estudiantes de pregrado con necesidad financiera. No necesita ser reembolsada. Hasta $7,395 por año.",
            "ht": "Bous federal pou elèv inivèsite ki gen bezwen finansyè. Pa bezwen ranbouse. Jiska $7,395 pa ane.",
        },
        "eligibility": {
            "en": "US citizens/eligible noncitizens with demonstrated financial need. Complete the FAFSA.",
            "es": "Ciudadanos estadounidenses/no ciudadanos elegibles con necesidad financiera demostrada. Complete la FAFSA.",
            "ht": "Sitwayen ameriken/moun ki pa sitwayen ki elijib ki gen bezwen finansyè demontre. Ranpli FAFSA a.",
        },
        "phone": "800-433-3243",
        "website": "https://studentaid.gov/understand-aid/types/grants/pell",
        "address": "Apply online at studentaid.gov",
        "level": "federal",
    },
    {
        "id": "edu-library",
        "category": "education",
        "name": {
            "en": "Miami-Dade Public Library System",
            "es": "Sistema de Bibliotecas Públicas de Miami-Dade",
            "ht": "Sistèm Bibliyotèk Piblik Miami-Dade",
        },
        "description": {
            "en": "50+ branches offering free internet, computer access, literacy programs, citizenship classes, homework help, and digital resources.",
            "es": "Más de 50 sucursales que ofrecen internet gratis, acceso a computadoras, programas de alfabetización, clases de ciudadanía y ayuda con tareas.",
            "ht": "Plis pase 50 branch ki ofri entènèt gratis, aksè òdinatè, pwogram alfabetizasyon, klas sitwayènte, èd devwa, ak resous dijital.",
        },
        "eligibility": {
            "en": "Free library card for all Miami-Dade residents. Just bring a photo ID and proof of address.",
            "es": "Tarjeta de biblioteca gratuita para todos los residentes de Miami-Dade. Solo traiga una identificación con foto y comprobante de dirección.",
            "ht": "Kat bibliyotèk gratis pou tout rezidan Miami-Dade. Jis pote yon ID ak foto ak prèv adrès.",
        },
        "phone": "305-375-2665",
        "website": "https://www.mdpls.org",
        "address": "101 W Flagler Street, Miami, FL 33130 (Main Library)",
        "level": "county",
    },
    {
        "id": "edu-education-fund",
        "category": "education",
        "name": {
            "en": "The Education Fund",
            "es": "The Education Fund",
            "ht": "The Education Fund",
        },
        "description": {
            "en": "Supports Miami-Dade public school students with college prep, scholarship matching, supply drives, and teacher grants.",
            "es": "Apoya a estudiantes de escuelas públicas de Miami-Dade con preparación universitaria, becas, suministros y subvenciones para maestros.",
            "ht": "Sipòte elèv lekòl piblik Miami-Dade ak preparasyon kolèj, bous, founiti, ak sibvansyon pou anseyan.",
        },
        "eligibility": {
            "en": "Miami-Dade public school students, teachers, and schools.",
            "es": "Estudiantes, maestros y escuelas públicas de Miami-Dade.",
            "ht": "Elèv, anseyan, ak lekòl piblik Miami-Dade.",
        },
        "phone": "305-558-4544",
        "website": "https://educationfund.org",
        "address": "Miami, FL",
        "level": "nonprofit",
    },
    # ── GENERAL / MULTI-CATEGORY ─────────────────────────────
    {
        "id": "general-211",
        "category": "general",
        "name": {
            "en": "211 Miami-Dade / Monroe Helpline",
            "es": "Línea de Ayuda 211 Miami-Dade / Monroe",
            "ht": "Liy Èd 211 Miami-Dade / Monroe",
        },
        "description": {
            "en": "24/7 helpline connecting residents to social services: housing, food, healthcare, utilities, mental health, disaster relief, and more.",
            "es": "Línea de ayuda 24/7 que conecta a residentes con servicios sociales: vivienda, alimentos, salud, servicios públicos, salud mental y más.",
            "ht": "Liy èd 24/7 ki konekte rezidan ak sèvis sosyal: lojman, manje, sante, sèvis piblik, sante mantal, ak plis ankò.",
        },
        "eligibility": {
            "en": "Available to anyone. Multilingual operators. Call 211 or text your zip code to 898211.",
            "es": "Disponible para todos. Operadores multilingües. Llame al 211 o envíe su código postal al 898211.",
            "ht": "Disponib pou tout moun. Operatè miltilingw. Rele 211 oswa voye kòd postal ou nan 898211.",
        },
        "phone": "305-358-4357",
        "website": "https://www.211miami.org",
        "address": "Dial 211 from any phone",
        "level": "county",
    },
]


def search_programs(
    category: str | None = None,
    query: str = "",
    language: str = "en",
    level: str | None = None,
) -> list[dict]:
    """Search the program database."""
    results = PROGRAMS
    if category:
        results = [p for p in results if p["category"] == category]
    if level:
        results = [p for p in results if p["level"] == level]
    if query:
        q = query.lower()
        results = [
            p
            for p in results
            if q in p["name"].get(language, p["name"]["en"]).lower()
            or q in p["description"].get(language, p["description"]["en"]).lower()
        ]
    return results


def get_program_by_id(program_id: str) -> dict | None:
    """Get a single program by its ID."""
    for p in PROGRAMS:
        if p["id"] == program_id:
            return p
    return None


def format_program(program: dict, language: str = "en") -> str:
    """Format a program for display."""
    lang = language if language in ("en", "es", "ht") else "en"
    name = program["name"].get(lang, program["name"]["en"])
    desc = program["description"].get(lang, program["description"]["en"])
    elig = program["eligibility"].get(lang, program["eligibility"]["en"])
    phone = program.get("phone", "")
    website = program.get("website", "")
    address = program.get("address", "")

    lines = [f"**{name}**", desc, ""]
    label_elig = {"en": "Eligibility", "es": "Elegibilidad", "ht": "Elijibilite"}
    lines.append(f"**{label_elig.get(lang, 'Eligibility')}:** {elig}")
    if phone:
        lines.append(f"📞 {phone}")
    if website:
        lines.append(f"🌐 {website}")
    if address:
        lines.append(f"📍 {address}")
    return "\n".join(lines)

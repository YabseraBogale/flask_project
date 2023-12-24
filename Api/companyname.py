from pprint import pprint
class CompanyName():
    def __init__(self):
        self.companyname=['ንብ ኢንተርናሽናል ባንክ','ኢንተርናሽናል ባንክ','Ethiopian Mineral Petroleum',
                        'Zemen Insurance','Bunna International Bank','ፀሀይ ባንክ','ብርሀን ባንክ',
                        'ERSODA Audit Service LLP','Ethiopian Insurance Corporation',
                        'Digital Marketing Officer','Kenera Trading','EthSwitch','ወጋገን ባንክ',
                        'Habesha Weekly Promotion','የኢትዮጵያ አየር መንገድ','Ethiopian Airlines',
                        'Addis Ababa Revenue Authority','Emerald International College','Awash Bank','Enat Bank',
                        'የኢትዮጵያ ብሮድካስቲንግ ኮርፖሬሽን','ወልቂጤ ዩኒቨርሲቲ','USAID/Ethiopia Collaborating, Learning & Adapting Activity ARC/GIS Systems',
                        'Tsehay Insurance','አድማስ ዩንቨርሲቲ','የፌደራል ፀረ ሙስና ኮሚሽን','School of Kibrewosen','Berhan Bank','Addis Collage','eTech',
                        'Addis Credit and Saving Institution','ንብ ባንክ','ቦረና ዩኒቨርስቲ','Oromia International Bank','የአዲስ አበባ ጉምሩክ',
                        'Includovate Research Center PLC','Nisir microfinance','Zemen Bank','WebSprix IT Solutions,PLC','ኦሮሚያ ህብረት','ፋና ብሮድካስቲንግ',
                        'ዳሽን ባንክ','WebSprix','Bunna Insurance','ኦሮሚያ ህብረት ስራ ባንክ','አበባ ውሀ እና ፍሳሽ ባለስልጣን',
                        'ፋና ትሬዲንግ','ሳፋሪ ኮም ኢትዮጲያ','ከነራ ትሬዲንግ በተለያዩ ፊልዶች','Wallet Microfinance Institution Share Company','Bank of Abyssinia',
                        'United Insurance','Abay Bank','ኦሮሚያ ኢንሹራንስ','Government of Canada','Industrial Parks Development Corporation','የገቢዎች ሚኒስቴር','Addis Credit and saving',
                        'የመንግስት ኮሚኒኬሽን አገልግሎት','የኢትዮጵያ ሲቪል ሰርቪስ ኮሚሽን','ዌብ ስፕሪክስ','Kenera Trading PLC','ድሮጋ ፋርማ ቢዝነስ ግሩፕ','Nib International Bank',
                        'Ethiopian custom commission','ጎህ ቤትች ባንክ','Ethiopia Commodity Exchange','Nib Insurance','Ethiopian Ministry of Revenues',
                        'Lucy Insurance','ሳፋሪኮምኢትዮጲያ','የፌደራል ሰነዶች ምዝገባ እና ማረጋገጫ','Ethiopian Aviation Academy',
                        'ኢንዱስትሪ ፓርክ ልማት ኮርፖሬሽን','Edge Communication Technology','Mekdela Amba University','BNT Industry',
                        'የኦሮሚያ ኢንጂነሪንግ ኮርፖሬሽን','Ethiopian Red Cross Society','ፀደይ ባንክ','CBE','ዘምዘም ባንክ','Wegagen Bank','የኢትዮጵያ መንገዶች ባለስልጣን',
                        'Global Bank','ሲኔት ሶፍትዌርስ ቴክኖሎጂ','Ethiopia Kaizen Institute','Amhara Bank','Addis International Bank',
                        'Wolkite University','Oromia Bank','Safaricom','Ahadu Bank','Federal Procurement and Property Disposal Service','ግሎባል ኢንሹራንስ','Sidama Bank','ቪዥን ፈንድ ማይክሮ ፋይናንስ',
                        'Red Cloud ICT Solutions PLC','Safaricom Telecommunications Ethiopia Plc','Jr petroleum plc','Dashen Bank',
                        'ራሚስ ባንከ','የኢትዮጵያ ንግድ ባንክ ማህበር','Top Link Technology','የኢትዮጵያ ነዳጅ አቅራቢ ድርጅት','የአዲስ አበባ ገቢዎች ቢሮ','ደቡብ ግሎባል ባንክ',
                        'አቢሲኒያ ባንክ', 'Hibret Bank','ፀሀይ ኢንሹራንስ','የኢትዮጵያ መድሀኒት አቅርቦት እና ፋንድ ባለስልጣን','Harvard University',
                        'Addis Ababa University','Ethiopian Shipping and Logistics Service Enterprise','Lami Kura Subsity',
                        'Ethio Engineeting group','አዋሽ ባንክ','Meklit Microfinance Institution','ኢቲ ስዊች','Premier Switch Solutions','ሳፋሪ ኮም',
                        'Microsoft','አሀዱ ባንክ','UNILEVER(NGO)','Heineken Breweries','አባይ ባንክ','Federal Industrial Park Development Corporation (IPDC)',
                        'Abay research guidance','University of Michigan African Presidential Scholars (UMAPS) Program',
                        'Addis College','እናት ባንክ','ኮፕሬቲቭ ባንክ','ቡና ባንክ','ስንቄ ባንክ','Debub Global Bank','አዋጭ ብድር እና ቁጠባ','ሳፋሪኮም ኢትዮጲያ',
                        'ቫስኮም ኢንጂነሪንግ','የኢትዮጵያ መርከብ ትራንስፖርት እና ሎጂስቲክ ድርጅት','University Of People','አዲስ አበባ ከተማ ካውንስል ፅ/ቤት',
                        'YWCA Ethiopia','XOKA IT Solution PLC','አትላስ ዩኒቨርስቲ ኮሌጅ','Tsehay Bank','ኢትዮጵያ ፖስታ','Prokal Technologies Solutions',
                        'Wallet Microfinance','ፀሃይ ባንክ','አባይ ኢንሹራንስ','DAF Tech Social ICT Solution','ኦሮሚያ ባንክ','ቡና ኢንሹራንስ','IE Networks Solutions PLC','WebSprix IT Solutions PLC',
                        'ጎህ ቤቶች ባንክ']
    def GiveCompanyName(self):
        return self.companyname
    

























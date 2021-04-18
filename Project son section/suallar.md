1.Translator ve assembler nedir?
     Translator
Translator mənbə kodunu (yüksək səviyyəli proqramlaşdırma dillərindən birində yazılmış bir proqram) kompüter prosessoru tərəfindən istifadə olunan obyekt koduna və ya sonrakı şərh üçün ara koda çevirən bir proqramdır.

Translatorun növləri:
Compiler
İnterpreter
Assemble

   Assemble 
Aşağı səviyyəli proqramlaşdırma dillərinə əsas nümunə Assembler dilidir. Bu dil bilavasitə maşın əmrləri ilə işləmək üçündür. Bu dildə hər bir maşın əmrinə xususi sumvolik adlar uyğun gəlir. Bununlada bilavasitə maşın əmrləri ilə işləmək kimi çətin prosesə ehtiyac qalmır. Assembler dilində kompüterin əməli yaddaşı ilə birbaşa işləmək olur. Bu dildən adətən drayver programları yaratmaq üçün istifadə olunur.

2.Reqem ve ededlerin 2 li say sistemine tercume olunmasi bilirik.Bes hərflər ve simvollar binary code-a nece tercume olunur?

   Herfleri binary code-a cevirmek ucun:
Hər hərf üçün hərflə uyğunlaşdırılmış ASCII rəqəm dəyərini axtarın.
Hər bir ASCII ədədi dəyəri üçün ikili saya çevirin.
Hər ikili say üçün ikili say dəyərini qeyd edin.


3.Günümüzdə istifadə olunan Js,PHP,Python və C# dillərində ortaq istifadə olunan data növləri:
Integer.
Floating-point number.
String.
Boolean.

4.Type Conversion ve Type Casting nədir? Hansı hallarda ehtiyac duyulur?

TYPE CASTING:
  1.Bir məlumat növü bir casting operatoru istifadə edərək bir proqramçı  tərəfindən başqa bir məlumat tipinə çevrilir.
  2.Uyğun olmayan məlumat tiplərinə uyğun məlumat tiplərinə də tətbiq edilə bilər.
  3.Məlumat tipini başqa bir məlumat növünə ötürmək üçün casting operatoru  lazımdır.
  4.Məlumat tipini başqa bir məlumat növünə çevirərkən təyinat məlumat növü mənbə  məlumat növündən kiçik ola bilər.
  5.Proqramçı tərəfindən proqram tərtibatı zamanı baş verir.
  6.Daha səmərəli və etibarlıdır.

Type Conversion ise:
  1.Bir məlumat növü bir kompilyator tərəfindən başqa bir məlumat tipinə çevrilir.
  2.Yalnız uyğun məlumat tiplərinə tətbiq edilə bilər .
  3.Bir casting operatoruna ehtiyac yoxdur.
  4.Təyinat məlumat növü mənbə məlumat növündən kiçik ola bilməz.
  5.Tərtibat tərtib zamanı edilir.
  6.Daha az səmərəli və daha az etibarlıdır.


5.Operator precedence nədir və əhəmiyyəti?
-----



6.Automatic Type Conversion ve Type Conversion Methodlar arasındakı fərqlər?

Automatic Type Conversion da  JS "səhv" bir məlumat növü ilə işləməyə çalışdıqda, dəyəri "doğru" bir növə çevirməyə çalışir.
Bir məlumat növü bir kompilyator tərəfindən başqa bir məlumat tipinə çevrilir.


7.Implicit ve Explicit type conversiton nədir?

Implicit type conversiton məcburetmə gizli şəkildə edilir. JavaScript səhv bir məlumat növündə işlədikdə, dəyəri doğru məlumat tipinə çevirməyə çalışacaqdır.

Explicit type conversiton tip çevirmə kodda açıq şəkildə developer tərəfindən edilir. JavaScript, növ çevirmə üçün daxili metodlar təqdim edir.


start JS

 #about array

- array.push - array sonuna yeni element elave edir
- array.unshift - array evveline yeni element elave edir
- array.pop -sonuncu elementi silir
- array.shift -ilk elementi silir
- array.indexof - secdiyimiz elementin sirasini gosterir
- array.lentgh - arrayin uzunluğun gosterir


#about math objects

- Math.max()
- Math.min()
- MAth.PI pi sayisi
- Math.pow(4,3) menasi 4 usdu 3 cavab 64
- Math.random() 0 ve 1 arasinda her hansi sayi cixarir
- Math.round() yuvarlaqlasdirma  mes: Math.round(2.7); //returns 3
- Math.sign() musbet ve ya menfi oldugun bildirir
- Math.sqrt() kok alma
- Math.abs() modul
- Math.floor(1.6) asagi yvarlaqsdirir
- Math.trunc() koku cixarir


JS practice

Hereket eden qutu[https://codepen.io/pakizer/pen/abpmXPw]
slider [https://codepen.io/pakizer/pen/YzNVEmv]

JS slider:


SQL 
Data types of SQL:
String
1.CHAR(size)- from 0 to 255
2.VARCHAR(size)-from 0 to 65535
3.BINARY(size)-Equal to CHAR(), but stores binary byte strings. 
4.VARBINARY(size)-Equal to VARCHAR(), but stores binary byte strings.
5.TINYBLOB-For BLOBs (Binary Large OBjects). Max length: 255 bytes.
6.TINYTEXT-Holds a string with a maximum length of 255 characters.
7.TEXT(size)-Holds a string with a maximum length of 65,535 bytes.
8.BLOB(size)-	For BLOBs (Binary Large OBjects). Holds up to 65,535 bytes of data
9.MEDIUMTEXT-	Holds a string with a maximum length of 16,777,215 characters
10.MEDIUMBLOB	-For BLOBs (Binary Large OBjects). Holds up to 16,777,215 bytes of data
11.LONGTEXT-	Holds a string with a maximum length of 4,294,967,295 characters
12.LONGBLOB-	For BLOBs (Binary Large OBjects). Holds up to 4,294,967,295 bytes of data

NUMERIC
1.BIT(size)-A bit-value type,from 1 to 64.The default value for size is 1.
2.TINYINT(size)-A very small integer.
3.BOOL-Zero is considered as false, nonzero values are considered as true.
4.BOOLEAN-Equal to BOOL
5.INT(size)-	A medium integer.
6.INTEGER(size)	-Equal to INT(size)


Date and Time Data Types
1.DATE	-A date. Format: YYYY-MM-DD.
2.DATETIME(fsp)-	A date and time combination. Format: YYYY-MM-DD hh:mm:ss.
3.TIME(fsp)	A time. Format: hh:mm:ss
4.YEAR-A year in four-digit format.

SQL Server Data Types
String Data Types:
char(n)	
varchar(n)	
varchar(max)	
text	
nchar	
nvarchar		 
nvarchar(max)		 
ntext	
binary(n)		 
varbinary
varbinary(max)	 
image

Numeric Data Types

bit		 
tinyint	
smallint	
int	
bigint	

                         #Python practice
 The sequence required to learn all programming languages

 1.Veriable- bir kompüter proqramında istinad və manipulyasiya ediləcək məlumatları saxlamaq üçün istifadə olunur.Yeganə məqsədi məlumatları yaddaşda etiketləmək və saxlamaqdır.

 2.Data types-bir dəyişənin hansı dəyər növünə malik olduğunu və səhv etmədən ona hansı növ riyazi, əlaqəli və ya məntiqi əməliyyat tətbiq edilə biləcəyini göstərən bir təsnifatdır. 

 3.Operators-kompüter proqramında ümumiyyətlə  hərəkəti və ya prosesi təmsil edən  simvoldur. Bu simvollar riyaziyyat və məntiqdən uyğunlaşdırıldı. Operator müəyyən dəyəri və ya operanı idarə edə bilir.

 4.Conditions-proqramçı tərəfindən yaradılan, proqramdakı hərəkətləri qiymətləndirən və doğru və ya yalan olduğunu qiymətləndirən ifadələrdir. If-then-else ifadəsi ifadənin qiymətləndirilməsinə əsaslanan şərti icraya imkan verir.

 5.Function-hərəkəti yerinə yetirmək üçün istifadə olunan, mütəşəkkil, yenidən istifadə edilə bilən  kod blokudur. Funksiyalar tətbiqiniz üçün daha yaxşı modulluq və yüksək dərəcədə kodun təkrar istifadəsini təmin edir. Print () və main () kimi müxtəlif funksiyaları artıq görmüsünüz.

 6.Data structure-kompüter proqramında məlumatların səmərəli saxlanması, əldə edilməsi və işlənməsi üçün əvvəlcədən təyin olunmuş formatıdır. Bəzi məlumat strukturları proqramlaşdırma dilinin daxili komponentidir, digərləri isə strukturdan istifadə edilməzdən əvvəl kitabxana və ya modul daxil edilməsini tələb edə bilər.

 7.Loops-kodun bir hissəsini istədiyiniz proses tamamlanana qədər müəyyən sayda təkrarlayan bir proqramlaşdırma elementidir. Təkrarlanan tapşırıqlar proqramlaşdırmada tez-tez rast gəlinir və dövrlər vaxta qənaət etmək və səhvləri minimuma endirmək üçün vacibdir.

        #Interpreter diller

 Interpreter diller -kodu hədəf maşın tərəfindən birbaşa tərcümə edilmir. Bunun əvəzinə fərqli bir proqram, yəni tərcüməçi, kodu oxuyur və icra edir

ex:
 1.Java script- can be considered both a compiled and an interpreted language because its source code is first compiled into a binary byte-code. This byte-code runs on the Java Virtual Machine (JVM), which is usually a software-based interpreter.
 2.Python- is an interpreted high-level general-purpose programming language.
 3.PHP.
 4.Ruby.

        #Compiler diller

 Compiler diller-Yüksək səviyyəli bir dildə yazılmış mənbə kodunu (məsələn, C ++) rəqəmsal kompüterin CPU tərəfindən başa düşülə bilən maşın dilindəki təlimatlara çevirən (tərtib edən) kompüter proqramı.Compiler diller error-checking və digər qabiliyyətləri olan çox böyük proqramlardır.      

 ex:C,C++,Go,Fortran,Pascal

       #High level diller

HIGH LEVEL- Yüksək səviyyəli bir dil kompüter proqramlaşdırmasını sadələşdirmək üçün hazırlanmış bir proqramlaşdırma dilidir. Yüksək səviyyəli mənbə kodu oxunması asan bir sintaksis ehtiva edir, daha sonra aşağı səviyyəli bir dilə çevrilir və bu, müəyyən bir CPU tərəfindən tanına və idarə edilə bilər. Ən çox yayılmış proqramlaşdırma dilləri yüksək səviyyəli dillər hesab olunur.

Ex:C,FRONTAN,PASCAL

        #A general purpose diller

A general purpose diller-Tətbiqetmə sahələrində geniş tətbiq olunan və müəyyən bir etki üçün ixtisaslaşdırılmış xüsusiyyətlərdən məhrum olan bir kompüter dilidir. Bu, müəyyən bir tətbiq sahəsi üçün ixtisaslaşmış bir domenə xas bir dildən (DSL) fərqli olaraq. Xətt həmişə kəskin olmur, çünki dil müəyyən bir domen üçün ixtisaslaşdırılmış xüsusiyyətlərə malik ola bilər, lakin daha geniş tətbiq oluna bilər və ya əksinə prinsipcə geniş tətbiqetmə qabiliyyətinə malik ola bilər, lakin praktikada əsasən müəyyən bir domen üçün istifadə olunur  

ex:C, Java, PHP,Python

CMD commands:
dir-list directory content.
cd-change directory
cmd	start command prompt
cls-clear screen
mkdir-create a new directory
rmdir / rd-delete directory



#### SERX94: Experimentation
#### title : Keywords Generation
#### author : Chedvihas Punnam
#### date : 11/22/2022


## Explainable Records
### Record 1
**Raw Data:** 
Column Name : "Content "                                                                                            
"value" :   amazon translate support office document whether organization multinational enterprise present many countries small startup hungry global success translate content local languages may endure challenge indeed text data often come many format process may require several different tool also tool may support language pair may convert certain document intermediate format even resort manual translation issue add extra cost create unnecessary complexity build consistent automate translation workflows amazon translate aim solve problems simple cost effective fashion use either aws console single api call amazon translate make easy aws customers quickly accurately translate text different languages variants earlier year amazon translate introduce batch translation plain text html document today happy announce batch translation also support office document namely docx xlsx pptx file define office open xml standard introduce amazon translate office document process extremely simple would expect source document store amazon simple storage service amazon bucket please note document may larger megabytes million character batch translation job process single file type single source language thus recommend organize document logical fashion store file type language prefix use either aws console starttexttranslationjob api one aws language sdks launch translation job pass job complete collect translate file output location let quick demo translate office document use amazon console first upload docx document one bucket move translate console create new batch translation job give name select source target languages define location document amazon format docx case optionally could apply custom terminology make sure specific word translate exactly way want likewise define output location translate file please make sure path exist translate create finally set aws identity access management iam role give translate job appropriate permissions access amazon use exist role create previously also let translate create one click create job launch batch job job start immediately little later job complete three document translate successfully translate file available output location visible console download one translate file open compare original version small scale use extremely easy use aws console translate office file course also use translate api build automate workflows automate batch translation previous post show automate batch translation aws lambda function could expand example add language detection amazon comprehend instance could combine detectdominantlanguage api python docx open source library detect language docx file pretty simple could also detect type file base extension move proper input location could schedule lambda function cloudwatch events periodically translate file send notification email course could use aws step function build elaborate workflows imagination limit get start start translate office document today follow regions us east n virginia us east ohio us west oregon europe ireland europe london europe frankfurt asia pacific seoul never try amazon translate know free tier offer million character per month first months start first translation request give try let us know think look forward feedback please post aws forum amazon translate send usual aws support contact.


**Prediction Explanation:** For the above given input these are the predicted keywords ['translate', 'data', 'service', 'amazon', 'aws']. For the above given text as we can see the input the keywords look very releant. As per my observation the blog is mostly related to amzon, aws , translate data using amazon translate service. So, as we can see the keywords predicted are relevant to the crux of the blog.

### Record 2
**Raw Data:** 
new trigger kernel panic diagnose unresponsive ec instance work systems deploy premise data center sometimes happen debug unresponsive server usually involve ask someone physically press non maskable interrupt nmi button freeze server send signal command controller serial interface yes serial rs command trigger system dump state freeze kernel file analysis file usually call core dump crash dump crash dump include image memory crash process system register program counter information useful determine root cause freeze today announce new amazon elastic compute cloud amazon ec api allow remotely trigger generation kernel panic ec instance ec senddiagnosticinterrupt api send diagnostic interrupt similar press nmi button physical machine run ec instance cause instance hypervisor send non maskable interrupt nmi operate system behaviour operate system nmi interrupt receive depend configuration typically involve enter kernel panic kernel panic behaviour also depend operate system configuration might trigger generation crash dump data file obtain backtrace load replacement kernel restart system control organisation authorize use api iam policies give example cloud system engineer specialists kernel diagnosis debug find crash dump invaluable information analyse cause kernel freeze tool like windbg windows crash linux use inspect dump use diagnostic interrupt use api three step process first need configure behavior os receive interrupt default windows server amis memory dump already turn automatic restart memory dump save also select default location memory dump file systemroot equivalent c windows access options go start control panel system advance system settings startup recoveryon amazon linux need install configurekdump kexec one time setup edit file etc default grub allocate amount memory reserve crash kernel example reserve add crashkernel amount memory allocate depend instance memory size general recommendation test kdump see allocate memory sufficient kernel doc full syntax crashkernel kernel parameter grub cmdline linux default crashkernel console tty console ttys n net ifnames biosdevname nvme core io timeout rd emergency poweroff rd shell rebuild grub configuration finally edit etc sysctl conf add line kernel unknown nmi panic tell kernel trigger kernel panic upon receive interrupt ready reboot instance sure include command user data script ami automatically configure instance instance reboot verify kdump correctly start documentation contain instructions operate systems one time configuration do ready second step trigger api machine aws cli sdk configure example return value cli expect terminal session open instance disconnect instance reboot reconnect instance find crash dump var crash third last step analyse content crash dump linux systems need install crash utility debug symbols version kernel note kernel version capture kdump find kernel currently run use uname r command collect kernel crash dump often way collect kernel debug information sure test procedure frequently particular update operate system create new amis control authorize send diagnostic interrupt control organisation authorize send diagnostic interrupt instance iam policies resource level permissions like example price additional charge use feature however instance continue run state receive diagnostic interrupt instance bill continue usual availability send diagnostic interrupt ec instance power aws nitro system.


**Prediction Explanation:** For the above given input these are the predicted keywords ['windows', 'price', 'data', 'amazon', 'kernel']. As per my understanding, the above data says something about windows server crash and some kernel panic behaviour, some amazon linux installation is used to rectify. So, the keywords windows, amazon, kernel look relevant to the data givven.

## Interesting Features
### Feature A
**Feature:** nword

**Justification:** The feature nword is the label given for each word in the data, for the model to give the word as input, as we cannot give categorical data to the model as input, each word is assigned with a label and a label is encoded. Here, the nword just represents the word, so varying it means we are chaning the word to predict weather it is keyword or not.

### Feature B
**Feature:** score

**Justification:** The feature score is the score allocated for each word depending on its occurence in the document and the corpus. The score is allocated using TfIdf vectorization. Now this score tells the importance of the word in the data. So, if we increase the score of a word, its probability of being a keyword increases, if we decrease the value of the score, the probability for this word to be a keyword becomes less.

## Experiments 
### Varying A
**Prediction Trend Seen:** If the value of A - nword is varied, as it is the label of the word, so it just represents the word, so increasing or its numerical value doesn't exactly correlate to the output, instead it means that we are just giving another word as input. However, for the word amazon, the label allocated is 141 among the given content as input. So 141 is nword value. In the given document amazon is keyword.The score of amazon is 6.55 . So for the input [[141,6.55]], the output is 1- which means that amazon is keyword. Now, if I increase the value to 150 and give it as input keeping the other feature constant, I got the output as 1, but from this we cannot make any conclusions beacasue changing the value of nword is just changing the input word, so the output which got predicted is for some other word in the input text - in this case the word with label 150 is "amortize". So, from this we cannot make any trend.

### Varying B
**Prediction Trend Seen:** If the value of B - score is varied, it is correlated to the output. When I increase the value of the score at some extent, it gives the output as 1. Output 1 means that the word is keyword, so it says that with the increase in the value of score, it is more probable that the word is a keyword. For the input [[4279,0.16]] the output is 0. The input here is "wednesday", 0.16 is the score of it. The output is 0 which means that, the word wednesday is not a keyword in the given input. Now I will increase the score of the word i.e; the input is [[4279,2.5]], I got the output as 1. This means that the word is now a keyword. So, it means that the probability of a word being keyword increases with increase in the value of the score, viceversa.

### Varying A and B together
**Prediction Trend Seen:** Now, if I increase both nword and score. 
Input1: [[119,0.08]]  - word for 119 is "alike"
output1: 0 - Word "alike" is not a keyword.
now increasing both values
Input2: [[250,3]]  - word for 250 is "ask" 
Output2: 1 - Word "ask" is a keyword. 

From the above outputs, we cannot make any trend because, increasing the nword value means changing the word, so if we change the word, the value of its score i.e; the second feature should automatically change according its respective score, however I have just increased its value to look the outputs.



### Varying A and B inversely
**Prediction Trend Seen:** NOw, if i decrease nword and increase the score.
Input1: [[119,0.08]]  - word for 119 is "alike"
output1: 0 - Word "alike" is not a keyword.
now increasing both values
Input2: [[100,3]]  - word for 100 is "aim" 
Output2: 1 - Word "aim" is a keyword. 

From the above outputs, we cannot make any trend because, decreasing the nword value means changing the word, so if we change the word, the value of its score i.e; the second feature should automatically change according its respective score, however I have just increased its value to look the outputs.


class Teacher:

    def __init__(self, *,full_name:str, achievements:list, academy:str, ext:list, conference:str, email:str):
        self.name = full_name
        self.last_name = full_name.split(' ')[1].lower()
        self.email = email
        self.achievements = achievements
        self.academy = academy
        self.ext = ext
        self.conference = conference

#blosser
email = 'Brian.Blosser@gpisd.org'
name = 'Brian Blosser'
achiv = [
"Telecommunications Business Management",
"DeVry University",
"Microsoft Office Master",
"Microsoft Certified Professional",
"Television Production Proficiency",
"CPR/First Aid/AED"
]
academy = 'Academy of Business and Communications'
ext = 'TSA (Technology Student Association) Co-Advisor\n I coach girls fast-pitch softball, am an avid Steelers fan. This is my 10th year teaching and 5th year at Dubiski. '
conf = 'Conference:1st Period/8:50 - 10:15'


blosser = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)
#burk
email = 'david.burk@gpisd.org'
name = 'David Burk'
achiv = [
"Bachelor of Fine Arts in Communication Design",
"University of North Texas",
"University of Texas Arlington",
"Certifications:",
"All-Level Art (PK-12)",
"Technology Applications (EC-12)"
]
academy = 'Academy of Business and Communications'
ext = 'Artist • Illustrator • Educator • Jedi \"The greatest teacher, failure is.\"'
conf = 'Conference: 2nd Period: 10:20-11:45'


burk = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)
#case
email = 'tyler.case@gpisd.org'
name = 'Tyler Case'
achiv = [
"Associates in Motion Picture Production",
"KD College"
]
academy = 'Academy of Business and Communications'
ext = "Tyler Case has been apart of the film industry for 10 years. He's worked on feature films in California and Oklahoma. He started his own production company right out of High School filming Weddings, Special Events, Sports Events, Music Videos and more. His passion for Film and TV has given him the opportunities to travel and see the world while doing what he loves most. He's an award winning filmmaker and currently working on a feature film that will have world wide distribution on Netflix, Redbox, and VOD.\n\n If it can be written or thought, It can be filmed. - Stanley Kubrick"
conf = 'Conference: 2nd Period/10:20 - 11:45'


case = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)
#chirstensen
email = 'curtis.christensen@gpisd.org'
name = 'Curtis Christensen'
achiv = [
"Auto Collision",
"WTI",
"I Car, ASE"
]
academy = 'Academy of Human Services and Transportation'
ext = 'SkillsUSA Advisor'
conf = 'Conference: 5th Period/8:50 - 10:15'


chirstensen = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)
#ervin
email = 'william.ervin@gpisd.org'
name = 'William Ervin'
achiv = [
"Aviator College Of Aeronautical Science & Technology",
"Commercial Pilot Single/Multi Engine Airplane",
"Flight Instructor Single/Multi Engine Airplane Instrument",
"Advanced Ground Instructor"
]
academy = 'Academy of Health Science and Engineering'
ext = 'Skills USA Aviation Advisor \n Fear has two meanings; Forget Everything And Run or Face Everything And Rise.'
conf = 'Conference: 8th Period/2:50 - 4:15'


ervin = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)
#harris
email = 'dartagnan.harris@gpisd.org'
name = "D'artagnan Harris"
achiv = [
"B.S. in Architecture",
"Texas Tech University",
"M.Ed in Sports Administration",
"Concordia University"
]
academy = ''
ext = "SkillsUSA Advisor, Teacher Leadership Committee, Teacher Mentor\n \nFor I long to see you, that I may impart unto you some spiritual gift to make you strong, that is that you and I may be mutually encouraged by each other's faith. - Romans 1: 11-12"
conf = 'Conference: 1st Period/8:50 - 10:15'



harris = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)

#head
email = 'jonathan.head@gpisd.org'
name = 'Jonathan Head'
achiv = [
"B.A. in History",
"University of Texas at Arlington",
"M.Ed. in Educational Leadership",
"University of Texas at Arlington",
"College Board AP Scorer",
"Automotive Service Excellence: Maintenance & Light Repair",
"CDL-School Bus Endorsement",
"Hunter Engineering Alignment & Balancing",
"College Board AP Scorer",
]
academy = 'Academy of Health Science and Engineering'
ext = 'Academy Lead, SkillsUSA Advisor \n This is my 25th year in GPISD.'
conf = 'Conference: 8th Period/2:50 - 4:15'



head = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)
#mccown

email = 'deirdre.mccown@gpisd.org'
name = 'Deirdre McCown'
achiv = [
"Trade and Industrial Teaching Cert.",
"Society of Broadcast Engineers Television Operator",
"Adobe Premiere Pro ACA",
"Final Cut Pro",
"Certified Commercial Drone Pilot Part 107"]
academy = "SkillsUSA Lead, AV Skills Advisor"
ext = "My mission in life is not merely to survive, but to thrive; and to do so with some passion, some compassion, some humor, and some style. **Maya Angelou"
conf = "Conference:1st Period/8:50 - 10:15"

mccown = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)

#pigg
email = 'james.pigg@gpisd.org'
name = 'James Pigg'
achiv = [
"BS in Mathematics",
"Texas Tech University"
]
academy = 'Math Department Chair\n Computer Science'
ext = 'Mr. Pigg is a graduate of Texas Tech University, receiving his B.S. in Mathematics with a minor in Electrical Engineering.  During his stay at Texas Tech, Mr. Pigg had several majors, including Electrical Engineering, Computer Science, Computer Engineering, Civil Engineering, and Mathematics.  Mr. Pigg has also completed over 40 graduate-level math hours at Texas Tech.'
conf = 'Conference: 6th Period/10:20 - 11:45'


pigg = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)

#womack
email = 'scott.womack@gpisd.org'
name = 'Scott Womack'
achiv = []
academy = 'Academy of Business and Communications'
ext = 'SkillsUSA Advisor\n "Do the best you can until you know better. Then, when you know better, do better." - Maya Angelou'
conf = 'Conference: 6th Period/10:20 - 11:45'


womack = Teacher(full_name=name, achievements=achiv, academy=academy, ext=ext, email=email, conference=conf)

teachers = [blosser, burk, case,
            chirstensen, ervin,
            harris, head, mccown,
            pigg, womack]

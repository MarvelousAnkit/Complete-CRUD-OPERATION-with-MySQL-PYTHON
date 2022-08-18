from datetime import date 
import mysql.connector as sql
mycon=sql.connect(host='localhost', user='root', password='12345678',database='hubnet')
mycur=mycon.cursor()

today = date.today()
print("********************Welcome To Hub Net Library *************************")
print("\t \t \t \t  \t \tToday's date:", today)

print("Press 1 To Create a new Account")
print("Press 2 for Login")
ch =int(input("Enter Your Choice :  "))
if (ch==1):
    u=(input("Enter Your UID Here : "))
    p=(input("Enter Your Full Name Here : "))
    a=(input("Enter Your Email Id Here : "))
    b=int((input("Enter Your Phone Number : ")))
    c=(input("Enter Your Password Here : "))
    d="insert into user values('{}','{}','{}','{}','{}')".format(u,p,a,b,c)
    mycur.execute(d)
    mycon.commit()
    print("\n")
    print("Account Has Been Created Successfully !!!")
elif (ch==2):
    u=input("Enter Your Email ID : ")
    p=input("Enter Your Password : ")
    s="Select * from user where Email_id ='{}'and Password='{}' ".format(u,p)
    mycur.execute(s)
    data = mycur.fetchall()
    if data:
        print("**********************login Successfull*********************")
    else: 
        print("Login Failed , Pls Create a new account") 
        quit() # Due To Wrong Detail Program Get Cancelled
print("\n")
print ("Thanks For Choosing HUB NET Library - Best Library In The Patna")
print("\n")
print("Press 1 to Update Account Detalis ")
print("Press 2 to Delete Your Account ")
print("Press 3 To Read Books")

ch2=int(input("Enter Your Choice : "))
if (ch2==1):
    print("Press 1 Update Password")
    print("Press 2 Update Email Address")
    print("Press 3 Update Mobile Number")
    print("Press 4 Update Name")
if (ch2==2):
    u=input("Enter Your Email : ")
    p=input("Enter Your Password : ")
    s= "DELETE FROM user WHERE Email_Id='{}' and Password='{}'".format(u,p)
    mycur.execute(s)
    mycon.commit()
    print("*******************Account Has Been Deleted Successfully *******************")
    quit()




if (ch2==3):
    print("\n")
    print("Press 1 To Read ABSALOM, ABSALOM! BY WILLIAM FAULKNER")
    print("Press 2 To Read A TIME TO KILL BY JOHN GRISHAM")
    print("Press 3 To Read THE HOUSE OF MIRTH BY EDITH WHARTON")
    print("Press 4 To Read EAST OF EDEN BY JOHN STEINBECK")
    print("Press 5 To Read THE SUN ALSO RISES BY ERNEST HEMINGWAY")
    print("\n")


    ch1=int(input("Enter Your Choice Here : "))
    if (ch1==1):
        print("\n")
        print("\t ***************************************************ABSALOM, ABSALOM! BY WILLIAM FAULKNER ***************************************************")
        print("\n")
        print("In 1833, a wild, imposing man named Thomas Sutpen comes to Jefferson, Mississippi, with a group of slaves and a French architect in tow. He buys a hundred square miles of land from an Indian tribe, raises a manor house, plants cotton, and marries the daughter of a local merchant, and within a few years is entrenched among the local aristocracy. Sutpen has a son and a daughter, Henry and Judith, who grow up in a life of uncultivated ease in the northern Mississippi countryside. Henry goes to college at the University of Mississippi in 1859, and meets a sophisticated fellow student named Charles Bon, whom he befriends and brings home for Christmas. Charles meets Judith, and over time, an engagement between them is assumed. But Sutpen realizes that Bon is actually his own son—Henry and Judith's half-brother—from a previous marriage which he abandoned when he discovered that his wife had negro blood. He tells Henry that the engagement cannot be, and that Bon is Henry's own brother; Henry reacts with outrage, refusing to believe that Bon knew all along and willingly became engaged to his own sister. Henry repudiates his birthright, and he and Bon flee to New Orleans. When war breaks out, they enlist, and spend four hard years fighting for the Confederacy as the South crumbles around them. At the end of the war, Sutpen (a colonel) finds his son and reveals to him that not only is Bon his and Judith's half-brother, he is also, in part, a black man.")
        
    if (ch1 ==2):
        print("\n")
        print("\t ***************************************************A TIME TO KILL BY JOHN GRISHAM ***************************************************")
        print("\n")
        print("This one is from 3:3 in the Ecclesiastes, again part of the Old Testament. The anonymous author is a King of Jerusalem who relates and analyses events in his own life. This has resonated strongly with a lot of people: Abraham Lincoln quoted Ecclesiastes when addressing Congress in 1862, and the novelist Thomas Wolfe called it ‘the greatest single piece of writing I have ever known.’ Grisham’s 1989 title is taken from the line that [To every thing there is a season, and a time to every purpose under the heaven:] A time to kill, and a time to heal; a time to break down, and a time to build up. After the festival ends, Jake, Mike, and Bill leave Pamplona. After a night in the south of France, Jake decides to return to Spain. He soon receives a telegram from Brett asking for help in Madrid. Jake immediately goes to Madrid, where he learns that Brett sent Romero away for fear of corrupting him. The novel ends unspectacularly, with Jake and Brett talking in a taxi in Madrid. In the final lines of the novel, Brett tells Jake she thinks they could have had a wonderful time together. Jake replies, “Yes, isn’t it pretty to think so?")
        

    if (ch1==3):
        print("\n")
        print("\t ***************************************************THE HOUSE OF MIRTH BY EDITH WHARTON ***************************************************")
        print("\n")
        print("Lily Bart, a beautiful but impoverished socialite, is on her way to a house party at Bellomont, the country home of her best friend, Judy Trenor. Her pressing task is to find a husband with the requisite wealth and status to maintain her place in New York society. Additional challenges to her success are her advancing age—at twenty-nine, she has been on the for more than ten years—her penchant for gambling at bridge that has left her with debts beyond her means to pay, and her efforts as part of upper-crust society to keep up appearances with her wealthy friends. Lily's choices are further complicated by her innermost desire to marry for love as well as money and status, and her longing to be free of the claustrophobic constrictions and routines of upper-crust society. Judy has arranged for her to spend more time in the company of Percy Gryce, a potential suitor who is wealthy but whom Lily finds boring. Lily grew up surrounded by elegance and luxury—an atmosphere she believes she cannot live without, as she has learned to abhor  The loss of her father's wealth and the death of her parents left her an orphan at twenty. Lacking an inheritance or a caring protector, she adapts to life as a ward of her strait-laced aunt Julia Peniston from whom she receives an erratic allowance, a fashionable address, and good food, but little direction or parenting. Lily is not fond of her aunt Julia and avoids her whenever possible while simultaneously relying on her for both necessities and luxuries.")
        
    if (ch1==4):
        print("\n")
        print("\t *************************************************** EAST OF EDEN BY JOHN STEINBECK ***************************************************")
        print("\n")
        print("Then he outlines the story of the warmhearted inventor and farmer Samuel Hamilton and his wife Liza, immigrants from Ireland. He describes how they raise their nine children on a rough, infertile piece of land. As the Hamilton children begin to grow up and leave the nest, a wealthy stranger, Adam Trask, purchases the best ranch in the Valley. Adam's life is seen in a long, intricate flashback. We see his tumultuous childhood on a farm in Connecticut and the brutal treatment he endured from his younger but stronger half-brother, Charles. Adam and Charles's father, Cyrus, was a Union Civil War veteran who was wounded in his very first battle and unable  to return to service; he nonetheless becomes an expert  who uses his intellectual knowledge of military affairs and wounded-veteran status to become a military adviser in Washington, D.C. As a young man, Adam spent his time first in the military and then wandering the country. He was caught for vagrancy, escaped from a chain gang, and burgled a store for clothing to use as a disguise. Later, he wires Charles to request $100 to pay for his travels home. Adam later sends money to the store to pay for the clothes and damage. After Adam finally makes his way home to their farm, Charles reveals that Cyrus had died and left them an inheritance of $50,000 each. Charles is torn with fear that Cyrus did not come by the money honestly. A parallel story introduces a girl named Cathy Ames, who grows up in a town not far from the brothers' family farm. Cathy is described as having a ; she is evil and delights in using and destroying people. She leaves home one evening after setting fire to her family's home, killing both of her parents. She becomes a whoremaster's mistress, but he beats her viciously upon realizing that she is using him and leaves her to die on Adam and Charles's doorstep. Charles sees through Cathy's facade, but Adam falls obsessively and irrationally in love and marries her. However, unbeknownst to Adam, Cathy seduces Charles at the time of her marriage and falls pregnant with twins, leaving open the question of whether Adam or Charles is the twins' father. She attempts and fails at a primitive abortion with a knitting needle. Adam newly wed and newly rich now arrives in California and settles with the pregnant Cathy in the Salinas Valley, near the Hamilton family ranch. Cathy neither wants to be a mother nor to stay in California. Though she warns Adam that she does not want to go to California and plans to leave as soon as she is able, Adam dismisses her, saying ")
        
    if(ch1==5):
        print("\n")
        print("\t ************************************************ THE SUN ALSO RISES BY ERNEST HEMINGWAY***************************************************")
        print("\n")
        print("A few weeks after their departure, the writer Bill Gorton (another of Jake’s friends) arrives in Paris. Together, Jake and Bill decide to go to Spain to attend the Fiesta de San Fermín in Pamplona, Spain, to see the running of the bulls and the bullfights. Before they leave, Jake and Bill run into Brett, who has recently returned from Spain, and her fiancé, Mike. Brett and Mike ask to accompany Jake and Bill to Pamplona. In private Brett reveals to Jake that she spent the last few weeks in Spain with Cohn. Bill and Jake take a train to the south of France, where they meet Cohn. Bill, Jake, and Cohn travel together to Pamplona, where they are eventually joined by Brett and Mike. They stay at a local hotel owned by a man named Montoya. Montoya is a bullfighting enthusiast, and he is eager to introduce the foreigners to the sport. Brett and Jake are especially captivated by the bullfights, and Brett is captivated by a 19-year-old bullfighter named Pedro Romero. While Mike, Cohn, and, incidentally, Jake spar over Brett, Brett runs off to Madrid with Romero.")
        
    quit() 










ch3=int(input("Enter Your Choice "))
if (ch3==1):
    u=input("Enter Your New Password : ")
    p=(input("Enter Your UID : "))
    s="update user set Name='{}' where UID='{}'".format(u,p)
    mycur.execute(s)
    mycon.commit()
    print("**********************PassWord Changed Successfully******************************** ")

elif (ch3==2):
    u=input("Enter Your New Email Address : ")
    p=(input("Enter Your UID : "))
    s="update user set Name='{}' where UID='{}'".format(u,p)
    mycur.execute(s)
    mycon.commit()
    print("******************************Email Address Changed Successfully******************************")

elif (ch3==3):
    u=input("Enter Your New Mobile Number: ")
    p=(input("Enter Your UID : "))
    s="update user set Name='{}' where UID='{}'".format(u,p)
    mycur.execute(s)
    mycon.commit()
    print("*********************************Mobile Number Changed Successfully******************************")

elif (ch3==4):
    u=input("Enter Your New Name :  ")
    p=(input("Enter Your UID : "))
    s="update user set Name='{}' where UID='{}'".format(u,p)
    mycur.execute(s)
    mycon.commit()
    print("***********************************Name Has Been Changed Successfully*****************************")








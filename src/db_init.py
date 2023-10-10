import os
from sqlalchemy import inspect
from blog import create_app, db, bcrypt
from users.models import User
from posts.models import Post


def init_db():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    app = create_app()
    
    with app.app_context():
        inspector = inspect(db.engine)
        if inspector.has_table("User"):
            print("Already exists...")
            return
        
        db.create_all()
        
        users = {
            1: {
                "name": "John Smith",
                "email": "johnsmith@example.com"
            }, 2: {
                "name": "Emily Johnson",
                "email": "emilyjohnson@example.com"
            }, 3: {
                "name": "Michael Davis",
                "email": "michaeldavis@example.com"
            }, 4: {
                "name": "Sarah Wilson",
                "email": "sarahwilson@example.com"
            }, 5: {
                "name": "David Brown",
                "email": "davidbrown@example.com"
            }, 6: {
                "name": "Jennifer Lee",
                "email": "jenniferlee@example.com"
            }, 7: {
                "name": "Christopher Taylor",
                "email": "christophertaylor@example.com"
            }, 8: {
                "name": "Jessica Martinez",
                "email": "jessicamartinez@example.com"
            }, 9: {
                "name": "Daniel Johnson",
                "email": "danieljohnson@example.com"
            }, 10: {
                "name": "Amanda Anderson",
                "email": "amandaanderson@example.com"
            }
        }
        
        posts = {
            1: {
                "title": "Exciting News!",
                "content": "We're thrilled to announce the launch of our new product line. Check out our website for more details and get ready to be amazed!"
            }, 2: {
                "title": "Important Update: Office Relocation",
                "content": "Attention all employees! We are moving to a new office location starting next month. Please check your email for more information regarding the move."
            }, 3: {
                "title": "Upcoming Event: Annual Charity Gala",
                "content": "Save the date! Our annual charity gala will be held on October 15th at the Grand Ballroom. Join us for an evening of elegance, entertainment, and giving back to the community."
            }, 4: {
                "title": "Customer Appreciation Sale",
                "content": "To express our gratitude for your continued support, we're offering a special customer appreciation sale. Enjoy exclusive discounts on your favorite products for a limited time. Happy shopping!"
            }, 5: {
                "title": "Job Opening: Marketing Manager",
                "content": "We're hiring a skilled and enthusiastic Marketing Manager to join our dynamic team. If you have a passion for marketing and a proven track record, apply now!"
            }, 6: {
                "title": "New Feature Alert: Dark Mode",
                "content": "Introducing dark mode for our mobile app. Experience a sleek and eye-friendly interface while conserving battery life. Update your app to enjoy this exciting new feature."
            }, 7: {
                "title": "Investment Opportunity: Tech Startups",
                "content": "Are you interested in investing in promising tech startups? Join us for an exclusive investor meetup on July 25th, where you can connect with innovative entrepreneurs and explore potential opportunities."
            }, 8: {
                "title": "Welcome to Our New Team Members",
                "content": "Let's extend a warm welcome to the newest members of our team: John, Sarah, and Lisa. We're excited to have them on board and look forward to their valuable contributions."
            }, 9: {
                "title": "Company-wide Wellness Program",
                "content": "We care about your well-being. Introducing our company-wide wellness program, designed to support your physical and mental health. Stay tuned for upcoming initiatives and activities."
            }, 10: {
                "title": "Limited Time Offer: Free Shipping",
                "content": "Good news for our online shoppers! For a limited time, enjoy free shipping on all orders above $50. Don't miss out on this great opportunity."
            }, 11: {
                "title": "Product Recall Notice",
                "content": "Attention all customers who purchased our XYZ product between July 1st and July 10th. A voluntary recall has been initiated due to a potential safety concern. Please visit our website for more details."
            }, 12: {
                "title": "Join Us at the Tech Conference",
                "content": "Calling all tech enthusiasts! We're participating in the upcoming Tech Conference on August 5th. Visit our booth to learn about our latest innovations and grab some cool swag."
            }, 13: {
                "title": "Holiday Office Closure",
                "content": "In observance of the upcoming holiday, our office will be closed on September 6th. We wish you all a joyful and relaxing holiday!"
            }, 14: {
                "title": "Stay Connected with Our Mobile App",
                "content": "Download our mobile app for easy access to our products, exclusive deals, and personalized recommendations. Stay connected with us wherever you go!"
            }, 15: {
                "title": "Volunteer Opportunity: Beach Cleanup",
                "content": "Join us this Saturday for a beach cleanup initiative. Together, we can make a difference in protecting our environment. Sign up now and help us create a cleaner and greener community."
            }, 16: {
                "title": "Save the Date: Company Retreat",
                "content": "Mark your calendars for our upcoming company retreat. It's a fantastic opportunity to recharge, bond with colleagues, and plan for the future. More details to follow soon."
            }, 17: {
                "title": "New Store Opening: Downtown Location",
                "content": "Exciting news for our city residents! We're delighted to announce the opening of our new store in downtown. Visit us on the grand opening day and enjoy exclusive discounts."
            }, 18: {
                "title": "Customer Satisfaction Survey",
                "content": "We value your feedback. Take a moment to complete our customer satisfaction survey and get a chance to win exciting prizes. Your opinion matters to us!"
            }, 19: {
                "title": "Employee Recognition: Outstanding Performance",
                "content": "Congratulations to our employee of the month, Jane Smith, for her exceptional performance and dedication. Thank you for your hard work and commitment to excellence."
            }, 20: {
                "title": "Tips for a Healthy Work-Life Balance",
                "content": "Finding the right balance between work and personal life is crucial. Check out our latest blog post for valuable tips on maintaining a healthy work-life balance."
            }, 21: {
                "title": "Important Notice: System Maintenance",
                "content": "Attention all users! We will be conducting system maintenance on July 20th from 10 PM to 2 AM. During this time, there may be intermittent service disruptions. We apologize for any inconvenience caused."
            }, 22: {
                "title": "Join Our Rewards Program",
                "content": "Unlock exclusive benefits and earn rewards with our new loyalty program. Sign up today and start enjoying the perks of being a valued customer."
            }, 23: {
                "title": "Charity Auction for a Good Cause",
                "content": "Participate in our charity auction and support a worthy cause. Bid on unique items and experiences while making a positive impact on the lives of those in need."
            }, 24: {
                "title": "Team Building Workshop: Enhancing Collaboration",
                "content": "We're hosting a team building workshop next week to foster collaboration and strengthen relationships among team members. Get ready for a fun and interactive session!"
            }, 25: {
                "title": "Stay Safe Online: Cybersecurity Tips",
                "content": "Protect yourself from online threats with our cybersecurity tips. Learn how to safeguard your personal information and stay safe in the digital world."
            }, 26: {
                "title": "Community Meetup: Networking Event",
                "content": "Expand your professional network and connect with like-minded individuals at our community meetup. Join us for an evening of networking, knowledge sharing, and building valuable connections."
            }, 27: {
                "title": "New Menu Launch: Exciting Flavors Await!",
                "content": "Calling all foodies! We're thrilled to unveil our new menu, featuring a delectable array of flavors and culinary delights. Visit us today and embark on a gastronomic adventure."
            }, 28: {
                "title": "Employee Training Program: Enhance Your Skills",
                "content": "Invest in your professional growth with our employee training program. Develop new skills, gain industry knowledge, and take your career to new heights."
            }, 29: {
                "title": "Environmental Sustainability Initiative",
                "content": "We're committed to protecting the environment. Learn about our sustainability initiatives and join us in creating a greener future for generations to come."
            }, 30: {
                "title": "Upgrade Your Wardrobe: Summer Fashion Collection",
                "content": "Get ready to turn heads this summer with our latest fashion collection. From vibrant prints to trendy accessories, discover the perfect outfits for the sunny season."
            }
        }
        
        db.session.commit()
        
        users_entities = [User(username=user["name"], email=user["email"], password=bcrypt.generate_password_hash(user["email"]).decode("utf-8")) for user in users.values()]
        db.session.add_all(users_entities)
        
        db.session.add_all([Post(title=post["title"], content=post["content"], author=users_entities[i%10]) for i, post in enumerate(posts.values())])
        
        db.session.commit()
        
        print("Created and populated tables successfully...")


def drop_db():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    app = create_app()
    
    with app.app_context():
        db.drop_all()
        
        print("Dropped all tables...")

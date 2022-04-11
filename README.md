# Johnpooch.dog

### Project Goals
This site was created for my good friend, John McDowell, to use as a platform to post articles on subjects he is passionate about in the world of tech.

## Live Instance

The live instance of this site can be found [here.](http://johnpooch.dog/)

## Overview

Johnpooch.dog is a blog website created using the Django framework. The styling of this website are based on the zen style of [Medium.](https://medium.com/) The structure and features are that of a typical blog website other than some extra features I've had to add in for correct funtionality of the site.

This website will be a place to read about all the languages, frameworks and technologies that John is interested in as a developer.

# User Experience (UX)

## Strategy

* User Goals
    * I want to be able to browse various articles on the site
    * I want an appealing and easy to navigate site

* Site Owner Goals 
    * I want the site to be accessible and responsive to allow users on all devices to be able to browse the site
    * I want the site to have interesting and engaging articles to build up an audience
    

## User Stories

* First Time Visitor 
    * I want to understand the main purpose of the site
    * I want to see an appealing and easy to navigate site
    * I expect the site to be accessible to all devices
    * I want to easily register for an account

* Unregistered Visitor
    * I want to be able to view all articles that are available for me to read
    * I want to be able to select and read individial articles

* Registered Visitor
    * I want to be able to log in and log out
    * I want to be able to comment under invididual articles
    * I want to be able to easily follow the author on GitHub and LinkedIn
    * I want to be able to change my password if I forget it
    * I want to recieve feedback that my comment is awaiting approval

* Superuser
    * I want to be able to add, delete or edit articles
    * I want to be able to approve and delete comments posted by registered users
    * I want to be able to delete a user
    * I want to be able to edit and delete tags
    * I want to have to ability to give give other users admin status
    
# Features

## Existing Features

- __The landing page__

    ![image](media/readme_screenshots/landing.png)

    - The landing page of this site is a simple one consisting of all the articles that have been written. What you will see is the image and an excerpt from the article.

- __The nav bar__

    ![image](media/readme_screenshots/header.png)

    - This site has a simple navbar consisting of site title which acts as a home button and depending on whether you're logged in or not, a login and register button or a logout button.
    - This is featured across all pages.

- __The footer__

    ![image](media/readme_screenshots/footer.png)

    - This site has a simple footer consisting of social media links to John's LinkedIn and GitHub.
    - This is featured across all pages.

- __The About__

    ![image](media/readme_screenshots/about.png)

    - The about section is a small and concise piece about who John is and what he is interested in and what you may see feature on the blog.

- __The comment section__

    ![image](media/readme_screenshots/commentox.png)

    - The site features a comment section that allows registered users to comment on the various posts on the site

    ![image](media/readme_screenshots/commentfeedback.png)

    - Once a registered user has posted a comment, they will be given feedback to show that the comment has been sent for moderation. Comments have to be approved by an admin to avoid inapropriate or unwanted comments.

    ![image](media/readme_screenshots/postedcomment.png)

    - Once the comment has been approved, it will be visible under the post on which it was posted.

- __Custom gist and code snippets__

    ![image](media/readme_screenshots/gist.png)

    ![image](media/readme_screenshots/codeblock.png)

    - This site uses [Django Summernote](https://github.com/summernote/django-summernote) which provides WYSIWYG editor for creating and editing blog posts. By default, Django Summernote escapes all HTML tags. This meant that embedding Gist scripts would not work as expected. To work around this, I wrote a function using the Regex library that looks for escaped gist scripts and replaces them with un-escaped script tags. Additionally, inline code-snippets are commonly added using back-ticks ("`code snippet`"). This behaviour is not natively supported by Django Summernote. To achieve this behaviour, the `parsed_content` method also replaces back-ticks with `<span>` tags that can be targeted in CSS to make them appear as code snippets. [Link to code.](https://github.com/mlenahan/ms4-django/blob/aa217116894a66741eeb9d2629f77b59cb40c5dd/blog/models.py#L48)

- __Authorisation__

    ![image](media/readme_screenshots/signup.png)

    - The site currently allows users to register for an account. Registering for an account will let users comment on individual articles.

    ![image](media/readme_screenshots/signin.png)

    - Registered users can sign into their accounts at this page. They can also sign out.

    ![image](media/readme_screenshots/passwordreset.png)

    - If a user has forgotten their password, they can reset it here.

    ![image](media/readme_screenshots/passwordresetconfirmation.png)

    - Users will recieve confirmation that an email has been sent to them for resetting their password.


## Features to implement

- __Email post notifications__

    - In the future, I would love to implement a feature that sends all registered users an email when a new article is posted. This would be a great way of letting all registered users know that a new article has been posted.

- __Password reset__

    - Currently the password reset function doesn't actually send and email to reset your password so this is a feature I defintely want to add in the future.
    

# Design

- __Colour Scheme__

    - As this is a blog site, I decided to use a simple monochromatic colour scheme. This creates a harmonious, visually cohesive look. It doesn't draw attention to itself and lets the content shine.

 - __Typography__

    - I used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site. I decided to use 'Martel Sans' as the primary font and 'Lora' as the secondary font.

- __Imagery__

    - All imagery for each article will be set by the author of the articles.

- __Design Choices__

    - The overall look and styling of this site is based on the zen styling of [Medium](https://medium.com/). I love reading articles on Medium and really enjoy the way they display their content so I took inspiration from this and applied it to my site.

# Technologies

## Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

1. [Google Fonts](https://fonts.google.com/)
2. [Font Awesome](https://fontawesome.com/)
3. [Git](https://git-scm.com/)
4. [GitHub](https://github.com/)
5. [Gitpod](https://www.gitpod.io/)
6. [Chrome devtools](https://developer.chrome.com/docs/devtools/)
7. [Heroku](https://dashboard.heroku.com/apps)
8. [Postgres](https://www.postgresql.org/)
9. [Django](https://www.djangoproject.com/)
10. [Autopep8](https://pypi.org/project/autopep8/)
11. [Django Summernote](https://github.com/summernote/django-summernote)
12. [Re](https://docs.python.org/3/library/re.html)


# Testing

Testing and results can be found [here](TESTING.md)

# Deployment

## Fork

- To fork this project, go to my [repository](https://github.com/mlenahan/Johnpooch.dog).

- Click the fork option displayed below.

![image](media/readme_screenshots/fork.png)

- The fork should now be in your repositories.

## Clone

- If someone wishes to clone the [repository](https://github.com/mlenahan/Johnpooch.dog), they can do so by using this command in their terminal/command line `git clone https://github.com/mlenahan/Johnpooch.dog.git`

- To install requirements, the user can use this command in their terminal/command line `pip3 install -r requirements.txt`





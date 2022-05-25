# Testing

## Automated Testing

The W3C Markup Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no syntax errors in the project.

-   ## [W3C Markup Validator](https://validator.w3.org/)

    - index.html
       * No errors found.

    ![image](media/testing_screenshots/index_validation.png)

    - post_detail.html
       * No errors found.

    ![image](media/testing_screenshots/post_detail_validation.png)

-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    
       ![image](media/testing_screenshots/css_validation.png)

       - Warnings due to use of CSS variables

       ![image](media/testing_screenshots/css_variables.png)

-   ## [Pep8 validation](http://pep8online.com/)

    - All python files have been passed through the pep8online validation service. Only one file contains errors and that is `test_models.py`. There are 7 'line too long' errors in this file. From my research, it is not good practice to split the name of a function so I have left them on one line. The 5 other errors occur in the test logic. I tried splitting the `escaped_content` and `expected_content` over several lines. This removed the 'line too long' errors but it broke my test cases so I reverted the changes to allow the tests to work as intended.

        - models.py

        ![image](media/testing_screenshots/modelspy.png)

        - admin.py
        
        ![image](media/testing_screenshots/adminpy.png)

        - apps.py
        
        ![image](media/testing_screenshots/appspy.png)

        - forms.py
        
        ![image](media/testing_screenshots/formspy.png)

        - test_models.py
        
        ![image](media/testing_screenshots/testspy.png)

        - urls.py
        
        ![image](media/testing_screenshots/urlspy.png)

        - views.py
        
        ![image](media/testing_screenshots/viewspy.png)

-   ## [JSHint](https://jshint.com/)

    - All JavaScript files have been passed through JSHint for validation. The only issues present are ES6 related warnings as JSHint doesn't support ES6 validation.

        - darkmode.js

        ![image](media/testing_screenshots/darkmodejsvalidation.png)

        - share.js

        ![image](media/testing_screenshots/sharejsvalidation.png)

-   ## Unit Testing 

    - I made the decision to unit test two functions in my project. `unescape_gist_embeds` and `substitute_code_snippets` in the `models.py` file. I decided that it is essential to ensure these functions work as intended as this site is a developer blog and will include many gists and code snippets.

        - To run the tests, enter the command `python3 manage.py test blog/tests` into your terminal/command line.

-    ## Testing User Stories

        - First Time Visitor

            - The main purpose of the site is clear. A first time visitor can clearly see that this is a blog style site.

            - The site is appealing and easy to navigate. The site has a clean, minimal monochromatic style and the nav bar is easy to navigate.

            ![image](media/testing_screenshots/testing_user_stories/user-story-main-purpose.png)

            - The site is accessible and responsive across all devices.

            Mobile

            ![image](media/testing_screenshots/testing_user_stories/user-story-mobile.jpg)

            Tablet

            ![image](media/testing_screenshots/testing_user_stories/user-story-tablet.png)

            - It is easy to register for an account. The register link is on the right side of the nav bar and the Sign Up form is easy to navigate.

            ![image](media/testing_screenshots/testing_user_stories/user-story-sign-up.png)
        
        - Unregistered Visitor

            - All available articles are present on the landing page of the site so they are easy to access and navigate. They are presented in reverse chronological order.

            ![image](media/testing_screenshots/testing_user_stories/user-story-view-all-available-articles.png)

            - By simply clicking the title of an article, the user will be brought to the article page therefore making it easy to select and read individual articles.

            ![image](media/testing_screenshots/testing_user_stories/user-story-read-article.png)

        - Registered User

            - It is easy to log in and logout of the site. The log in button is located on the right side of the nav bar. Once logged in. the logout button will be located on the right side of the nav bar. This allows for easy loggin in and loggin out.

            ![image](media/testing_screenshots/testing_user_stories/user-story-sign-in.png)

            ![image](media/testing_screenshots/testing_user_stories/user-story-log-out.png)

            ![image](media/testing_screenshots/testing_user_stories/user-story-sign-out2.png)

            Feedback is given once you have signed out making it clear your action was successful

            ![image](media/testing_screenshots/testing_user_stories/user-story-sign-out3.png)

            - It is easy for a registered user to comment under individual posts. The comment box is clear and simple to use.

            ![image](media/testing_screenshots/testing_user_stories/user-story-commentbox.png)

            - Once a comment is posted, feedback is provided to the user showing their actioan was successful and is awaiting approval.

            ![image](media/testing_screenshots/testing_user_stories/user-story-comment-feedback.png)

            - Icons with links to the authors GitHub and LinkedIn are present in the footer of the site and above each individual post allowing for the user to easily follow the author on these platforms

            ![image](media/testing_screenshots/testing_user_stories/user-story-socials.png)

            ![image](media/testing_screenshots/testing_user_stories/user-story-socials2.png)

            - If a registered user wants to change their password, they can easily do so by navigating to the change password page.

            ![image](media/testing_screenshots/testing_user_stories/user-story-passwordreset.png)

            Once the user has reset their password, feedback is provided to show their action was successful

            ![image](media/testing_screenshots/testing_user_stories/user-story-passwordresetconfirmation.png)
        
        - Superuser

            - It is simple for a superuser to add, delete and edit articles.

            ![image](media/testing_screenshots/testing_user_stories/user-story-superuser-article.png)

            - It is simple for a superuser to approve and delete comments posted by a registered user.

            ![image](media/testing_screenshots/testing_user_stories/user-story-superuser-comment.png)

            - It is simple for a superuser to delete a user.

            ![image](media/testing_screenshots/testing_user_stories/user-story-superuser-user-delete.png)

            - It is simple for a superuser to edit or delete tags.

            ![image](media/testing_screenshots/testing_user_stories/user-story-superuser-tag-edit.png)

            - It is simple for a superser to give other users admin status.

            ![image](media/testing_screenshots/testing_user_stories/user-story-superuser-give-admin-status.png)
            

## Bugs

-   ### Fixed Bugs

- This site uses [Django Summernote](https://github.com/summernote/django-summernote) which provides WYSIWYG editor for creating and editing blog posts. By default, Django Summernote escapes all HTML tags. I wrote two custom functions to fix this bug. See features section in the [README.md](README.md) for more detail.

-   ### Unfixed Bugs

- Since the site uses Django Oauth for authorisation, my `SiteSettings` model is unusable(or I'm just unsure how to use it) in the Django Oauth templates meaning the title that acts as a home button does not appear when using these pages.

![image](media/testing_screenshots/sitesetting.png)

## Responsiveness

My site is responsive accross all devices as far as I am aware.

- ### Desktop

![image](media/readme_screenshots/landing.png)

- ### Tablet

    - Tablet landscape

    ![image](media/testing_screenshots/tablet_landscape.png)

    - Tablet portrait

    ![image](media/testing_screenshots/tablet_portrait.png)

- ### Mobile

    - Mobile landscape

    ![image](media/testing_screenshots/mobile_landscape.jpg)

    - Mobile portrait

    ![image](media/testing_screenshots/mobile_portrait.jpg)

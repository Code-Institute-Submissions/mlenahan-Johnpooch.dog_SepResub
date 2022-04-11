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

-   ## Unit Testing 

    - I made the decision to unit test two functions in my project. `unescape_gist_embeds` and `substitute_code_snippets` in the `models.py` file. I decided that it is essential to ensure these functions work as intended as this site is a developer blog and will include many gists and code snippets.

        - To run the tests, enter the command `python3 manage.py test blog/tests` into your terminal/command line.

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

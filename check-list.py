import streamlit as st
import json

st.set_page_config(layout= 'wide')

st.markdown('# Production Readiness Checklist')

checklist, details, notes, sources = st.tabs(['Checklist', 'Details', 'Other Notes', 'Sources'])
 
CHECKLIST_STRING = """
Common Checklist
☑ Clean Code
☑ Documentation
☑ Architecture
☑ Testing
☑ Error Handling
☑ Logging
☑ Validation
☑ DevOps
☑ Application Monitoring
☑ Support Channels

Common (Optional)
☑ Feature Flags
☑ Profiling
☑ Mapping

Server Checklist
☑ Configuration
☑ Data Storage
☑ Data Seeding
☑ Querying
☑ Analytics
☑ Abuse

Server (Optional)
☑ Email
☑ Identity
☑ Exporting
☑ File Storage
☑ Background Services
☑ Real Time Communication
☑ Audit Trails

Client Checklist
☑ Localization
☑ Application Icons
☑ Service Access
☑ Responsive Interface
☑ Accessibility
☑ Forms
☑ Regulations
☑ Shell Integration
☑ Web Support

Client (Optional)
☑ Offline
☑ Data Virtualization
☑ Themes
☑ Printing
☑ SPA Support
☑ Third-Party Clients
"""

DETAILS_STRING = """
Common Checklist
These are the conventions to apply to every application, whether they are running on the server or the client.

Clean Code
Clean code is a big topic by itself. But you can get yourself off on the right foot with linters / analyzers. For .NET I add the following to all my projects:

A starting .editorconfig file.
Roslynator — A extended collection of Rosyln analyzers.
AsyncFixer — Finds and corrects common misuses of async/await.
Enable Null Safety.
A Guard Clause library — Helps for defensive programming by validating input parameters.
There are other options available to Visual Studio users. This means every developer must have it installed and its only available in Visual Studio, not Visual Studio Code or Visual Studio for Mac, which limits its appeal in team environments.

CodeMaid — This Visual Studio add-in brings code cleaning, formatting, and organizing to your files. The configuration can be store in the solution.
Code Cleanup on Save — Use this extension to apply code cleanup rules on every save. The cleanup profile used has all options applied. Unfortunately, at this time, these options can’t be stored in a solution.
An alternative that provides similar functionality is JetBrain’s Rider. It’s cross platform which opens it to more developers, but it's not free and locks everyone into the same IDE if you want to rely on it.

Documentation
At a minimum, create a README.md file with the following:

A description of the project.
How to get your project up and running.
Guidelines for contributing code.
Your clean code standards.
A high-level description of the architecture.
The features you have implemented in your code. These are not business rules, but technology features like logging and null safety.
Learning resources for the major technology included in your project.
You should also consider creating a more complete Wiki over time.

Architecture
Decide on basic architectural patterns for your application and stick with them to make the application consistent. For a small application, a service layer for CRUD commands is usually enough. For larger applications I like to use the Clean Architecture Domain Drive Design patterns. For the largest and most complex applications consider a micro services approach. Serverless is also another popular option.

Testing
Do not skip automated testing. You should at least have unit testing, but you may want to go further and include integration, system, end to end, performance, penetration, etc.

My test projects tend to follow these patterns:

xUnit based.
Organized in folders that match the project namespaces.
Use a Given / Should naming convention. Ex: Method_GivenSomeCondition_ShouldReturnThisValue.
Follow the Act, Arrange, Assert pattern.
Use Fluent Assertions for readability, which also come with an analyzer to make sure you are using them correctly.
Add a mocking library. I prefer NSubstitute.
Error Handling
Your application should never hard crash. Make sure you catch all your errors, log them, and display a helpful error message. This is true if the error happens on the server or the client. A global error handling strategy is necessary.

Logging
Every application needs to log events. Consider Serilog for this. Make sure logging is happening on the server and the client. Serilog has “sinks” you can setup to record your logs to files, the Event Manager, a database and Application Insights.

Validation
Don’t let bad data into your app and don’t let bad data produce an error. All data coming in should be properly validated and report back if the data is not valid before it can be saved.

In .NET this is usually achieved using Data Annotations or Fluent Validation.

DevOps
Setup your code repository to compile your code and execute your tests automatically for pull requests with something like GitHub Actions. Then setup a strategy for deploying your code to users, if necessary, with something like Visual Studio App Center.

Application Monitoring
Don’t let problems with your application go unnoticed. Build in application monitoring from the start. Something like Application Insights works well for this.

Support Channels
Plan ahead for how your users will contact you for support. Will they simply use an email address? Or do you want more interaction through GitHub Discussions, a Discord server, social networks, or forums?

Common (Optional)
Feature Flags — At some point you may want to roll out a feature slowly and deprecate code over time. Feature Flags are an effective way to manage this.

Profiling — Want to know what’s taking so long on a specific page or action? Profiling is your ticket. There are tools baked into IDEs to help with this or you can setup automated tests to keep an eye on it. But if you want an integrated profiler testers and developers can access, look for something like Mini-Profiler.

Mapping — If you are copying data between object frequently such as between entities and view models, you should invest in an object mapper like AutoMapper.

Server Checklist
These are the conventions to apply to server-based applications like APIs.

Configuration
Setup your configuration settings so they can be specific to the environment they are running on. And store any sensitive information like passwords and keys in secure store like User Secrets or Azure Key Vault.

Data Storage
Will you support more than one configurable database type like both SQLite and SQL Server? Will you use an ORM like Entity Framework? Should you enable or disable cascading deletes?

Data Seeding
Load your application when it is running in development and test environments with sample data so you can better see how your application looks and performs from a non-blank slate. Consider Bogus for this.

Querying
Whether your application is server-side pages like MVC, or an API, you need a strategy to allow the controllers to query data from inbound parameters. This usually includes paging, searching, sorting, and filtering. You can manage this yourself or turn to a library like oData or GraphQL.

Analytics
Know how your application is being used beyond basic logs. Application Insights works well for this as already mentioned above for Application Monitoring.

Abuse
How will you protect your interface from clients sending in too many requests? Do you need some sort of rate throttling?

Server (Optional)
Email — You may need email when you are running a server. You can certainly send them through an email services like Outlook, but you should also look at a dedicated service like SendGrid. You can make sending emails easier with a package like FluentEmail.

Identity — Authentication is hard. Microsoft has baked it into its templates and there are a lot of third party options. You need to handle registration, login / logout, role or claims based authorization, token refreshing, password resets, email verification, user lockout, two-factor authentication, social logins, QR codes, biometrics, and more. Did I mention that authentication is hard?

Exporting— Sometimes your uses just want to take their data with them in Excel, Word or PDFs. Make it easy.

File Storage — File storage is different from data storage. In general, you don’t want to store them in the database. This is what file systems and Blob storage are for. Don’t forget to have a cleanup strategy for temporary or abandoned files if necessary.

Background Services — If you need something running in the background kicking off jobs look to Hangfire or Azure Functions.

Real Time Communication — WebSockets and SignalR are your friends.

Audit Trails — In some cases, usually multi-user applications, you may want to store a record of every change that is made and possibly be able to undo changes based on the trail. This can be done with custom code or using a feature of the database such as Change Data Capture or Temporal Tables.

Client Checklist
These are the conventions to apply to client-based applications and web pages.

Localization
Not everyone speaks your native language. If you think there is a chance you need to support multiple languages, put in good globalization practices right away.

Application Icons
Don’t use the default generic icon. Get a custom icon and make sure you set them for whatever environments you need to support, like favicons and home screens.

Service Access
If you are going to access an API or any other data source that is external to the client, build in fail safes when they are slow or down. Polly works well for this.

Responsive Interfaces
Evaluate your application on a variety of screen sizes and types. Going beyond standard screens like TV and Dual Screen can make your application stand out.

Accessibility
Don’t forget your users that might have different abilities and needs.

Forms
Forms are easy and hard. Make sure you have a good client validation strategy, you prevent double posting, manage dirty form navigation, and prevent overcommunicating with services on controls like auto complete.

Regulations
Does your application live in an industry that is regulated? Know those regulations and make sure your application meets them. GDPR is a common example.

Shell Integration
Look for ways to make your application take advantage of the client’s native services like Notifications, 3D Touch, Timeline, Widgets and Live Tiles. Even simple things like the window title or proper page titles on the web.

Web Only
Errors — Add a custom error, not authorized, and not found page.

Lighthouse — A great tool for checking performance, best practices, accessibility, and SEO.

Client (Optional)
Offline — How will you store data on the client?

Data Virtualization — Do you have a lot of data and only want to load what’s being shown on the screen? This goes beyond paging.

Themes — Do you want to support themes and have them match the OS theme? Should you provide a more compact mode?

Printing — Will users want to print your application’s data or views?

SPA Only — Hosting model (client / server / progressive web app / hybrid / native), lazy loading, pre-rendering and AOT compilation.

Third-Party Clients — Should you integrate with third party clients like those applications found in Microsoft 365?
"""

SOURCES_STRING = """
https://www.techtarget.com/searchsoftwarequality/tip/A-production-readiness-checklist-for-software-development

https://www.infoq.com/presentations/production-ready-applications/

https://www.getport.io/blog/production-readiness

https://www.cortex.io/post/how-to-create-a-great-production-readiness-checklist?utm_source=google-ppc&utm_campaign=21034493443&utm_medium=ppc&utm_content=691191339553&utm_term=production%20readiness%20checklist&gad_source=1&gclid=CjwKCAjw1K-zBhBIEiwAWeCOF4-iIJaiCDP6ZNDW_x3ZvwJoVvDVN6tkvrnyHh-XtbQxRMAzNQogbhoC-AIQAvD_BwE

https://scottkuhl.medium.com/building-production-ready-applications-24405c706707
"""

NOTES_STRING = """
- stability and reliability 
- scalability 
- performance
- fault tolerance and disaster recovery 
- monitoring 
- documentation 

- Caching: The best way to prevent performance issues is to enable caching on your application.You can use S3 file storage for caches.
- Static Files: If you have static files, it is best to store the files in S3 or point CloudFront to an assets folder so you serve your assets with a CDN.

- what's my unit test coverage percentage
- Has this code base been built recently
- check that you are using the best practice library for something
- Service Score Card
An internal developer portal can implement a scorecard system that tracks production readiness and additional KPIs and health checks.

- potential vulnerabilities;
- proper authorization and authentication techniques;
- data encryption (both at rest and in flight); and
- Another vital security element to consider as part of predeployment QA is penetration testing, which determines if known tools and techniques can hack a build.

- There is no one definition for “production-ready”. It’s a spectrum, and production readiness is slightly different for every organization and its needs. For example, a “production-ready” service for an early-stage startup might only require monitoring support, alerts, and a few unit tests. In contrast, in a large corporation, production readiness may be an adequate amount of unit and integration tests, documentation, monitoring, alerts, tracing support, and more.
"""

checklist_status = {}

with checklist: 
    # Persists across sessions
    with open('checklist_status.json', 'r') as file: 
        checklist_status= json.load(file)
    #st.write(checklist_status)

    for item in CHECKLIST_STRING.split('\n')[1:]: 
        if '☑' not in item: 
            st.markdown(f'#### {item}'.replace('Checklist', ''))
        else: 
            item = item.replace('☑', '')
            checked = st.checkbox(item, value=checklist_status.get(item, False))
            if checked: 
                checklist_status[item] = True
            else: 
                checklist_status[item] = False
    
    # Persists across sessions
    #st.write(checklist_status)
    with open('checklist_status.json', 'w') as file: 
        json.dump(checklist_status, file)

with details:
    for line in DETAILS_STRING.split('\n')[1:]:
        if '.' not in line and len(line.split(' '))<3:
            st.markdown(f'#### {line}'.replace('Checklist', ''))
        else: 
            st.write(line)

with notes: 
    st.write(NOTES_STRING)

with sources: 
    for num, source in enumerate([item for item in SOURCES_STRING.split('\n') if item]):
        st.markdown(f'{num+1}. {source}')



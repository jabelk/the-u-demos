 
If you have worked on an infrastructure team, you probably have run across someone who built scripts for the team to use. The scripts may have done things like verify connectivity or make some simple change that the team is required to do often. The term "script" is often used casually to refer to an executable file that accomplishes a simple task. Scripts are denoted by the programming language used to write them, such as a Python script, a standalone executable file that uses Python to accomplish the task. Other common scripting languages are Bash and Perl.

Some of the attributes of a Python script are:

- Standalone file (or directory)
- Purpose-built for the business need
- Not imported into a larger framework or library
- Often executable with command-line parameters for users who don't need to understand how it works

Some of the benefits of building a Python script are:

- Easier to maintain because it is focused on a business purpose and often not used by other code bases
- Helps many other engineers who may not need or want to code but can use the script
- Often easier to write and put into production than more comprehensive solutions

Some of the pitfalls of building a Python script are:

- If the business purpose changes, they are often difficult to maintain and end up not being used anymore.
- They can be difficult to reuse or extend for use cases that are adjacent or similar, depending on the design.
- They encourage a small number of maintainers; if those maintainers leave the company, the script goes to waste.

---

title: "Python Scripts vs. Modules"
date: 2023-02-06
description: "Have you ever wondered whether if __name__ == '__main__' actually matters? In this tutorial, you will build some simple scripts and see the difference in action!"
categories: [ Coding ]
tags: [ python ]
duration: 11:00
authors: Jason Belk
draft: false
ia-guid: a6ece804-7193-4693-9cf4-1bcc94146244
lesson-guid: 8891de6c-9ef3-4270-8b2a-9e66d813a0f6
certifications: null
technologies: null
skilllevels: null
---

<!-- MANDATORY STEP: Overview Step is a required step and must be at the beginning of each codelab -->
{{<step label="Overview" duration="1:00" xy-guid="cc6eae1e-fe3a-425b-bef6-1f933e09cb63">}}

Show how importing code without dunder main causes it to run.

### What You’ll Learn

- What are Python scripts?
- What are Python modules?
- How to use `__name__ == "__main__"`

### What You'll Need

- Basic understanding of Python
- Access to Python version 3.6+

{{</step >}}

<!-- When defining steps, Make sure there is no spaces between the brackets { {< >} } -->
{{<step label="What are Python Scripts?" duration="2:00" xy-guid="1211ed8c-6f69-45ce-93b9-3cbc2ae97092">}}

If you have worked on an infrastructure team, you probably have run across someone who built scripts for the team to use. The scripts may have done things like verify connectivity or make some simple change that the team is required to do often. The term "script" is often used casually to refer to an executable file that accomplishes a simple task. Scripts are denoted by the programming language used to write them, such as a Python script, a standalone executable file that uses Python to accomplish the task. Other common scripting languages are Bash and Perl.

Some of the attributes of a Python script are:

- Standalone file (or directory)
- Purpose-built for the business need
- Not imported into a larger framework or library
- Often executable with command-line parameters for users who don't need to understand how it works

Some of the benefits of building a Python script are:

- Easier to maintain because it is focused on a business purpose and often not used by other code bases
- Helps many other engineers who may not need or want to code but can use the script
- Often easier to write and put into production than more comprehensive solutions

Some of the pitfalls of building a Python script are:

- If the business purpose changes, they are often difficult to maintain and end up not being used anymore.
- They can be difficult to reuse or extend for use cases that are adjacent or similar, depending on the design.
- They encourage a small number of maintainers; if those maintainers leave the company, the script goes to waste.

{{</step >}}

{{<step label="What are Python Modules?" duration="2:00" xy-guid="2ab1290a-db0f-400b-95b8-d6974569a908">}}

Python modules are Python files that are written with a modular programming mindset. Rather than putting everything in one big file, the files are broken up into smaller and more focused files called "modules." To a new Python developer, both a module and a script may look alike because they are both Python files (.py) and have Python code to execute. A whole course could be written on Python package management and modules, but this tutorial will focus on the practical pieces with respect to modules versus scripts in the life of an infrastructure engineer.

Some of the attributes of a Python module are:

- If the code in the module is imported, it will not execute anything.
- Each module is not meant to be run on its own but is imported into another executable Python file, often called "main.py."
- The code is often broken up into a series of functions or classes that have descriptive names and parameters, so they are easy to identify when imported.

Some of the benefits of building a Python module are:

- Simpler to maintain and easier to delegate development to other teammates
- Easier to reuse code across multiple projects (some functions or features can be designed to be independent of the use case like authentication or logging)
- Testing is often easier; each module can be tested individually with mock inputs and expected outputs.

Some of the pitfalls of building a Python module are:

- Newer developers might struggle to follow the code because it is broken up across multiple files or directories.
- Introducing import statements also introduces the problem of pathing and importing the right module.

{{</step >}}

{{<step label="How to use __name__ == __main__" duration="6:00" xy-guid="7d203c72-af79-48eb-9e8a-462615867245">}}

Whether you are building a Python script or a Python module, it is important to know the value of using `if __name__ == "__main__":` in your code. First, let us look at a simple example.

## First Script Example

In your text editor, open up a new file called `my_script.py` with the following contents:

```python
# Build report
print("Gathering Data")
data = 42
second_data = 1337
print("Building report!")
data_report = [data, second_data]
print("Report Built.")
print("The report is ")
print(data_report)

# Send report
print("Loading Report")
print("...")
print("...")
print("Report Sent")

```

Try running the code above. You should get the following output:

```python
$ python my_script.py
Gathering Data
Building report!
Report Built.
The report is
[42, 1337]
Loading Report
...
...
Report Sent
$
```

The code is simple and printing mock output for the sake of simplicity. You can imagine much more complex code that accomplished the same thing with API calls and leveraging Python's many libraries.

When people are first learning Python, this is often how they write their code, all in one file, with sequential statements executing from top to bottom. They may use comments to indicate where a new logical piece begins, but nothing is abstracted into functions or classes because it just works.

## Module Example

Now imagine that you are given the script above and asked to reuse the code in a new report-building Python package. You have multiple teams' scripts that you need to compile into a single report.

Open a new file in the same directory as the `my_script.py` file, calling the new file `my_module.py` with the following contents:

```python
from my_script import data, second_data

new_data = 9999
compiled_data = [data, second_data, new_data]
print("Now building Compiled Report")
print(compiled_data)
print("...")
print("Now sending Compiled Report")

```

Run the `my_module.py` module. The output should look like this:

```python
$ python my_module.py
Gathering Data
Building report!
Report Built.
The report is
[42, 1337]
Loading Report
...
...
Report Sent
Now building Compiled Report
[42, 1337, 9999]
...
Now sending Compiled Report
$
```

Note that even though we were merely importing the two variables `data` and `second_data`, because `my_script` was written as one long sequential set of instructions, the importation also executed the other lines of code (including the print statements, for example).

## New Script with __main__

One huge thing missing in `my_script.py` is using `if __name__ == "__main__":` in the code and abstracting the execution into classes or functions.

Create a new Python file in the same location as the other ones called `my_script_with_main.py`, with the following contents:

```python
def build_report():
    print("Gathering Data")
    data = 42
    second_data = 1337
    print("Building report!")
    data_report = [data, second_data]
    print("Report Built.")
    print("The report is ")
    return data_report

def send_report():
    print("Loading Report")
    print("...")
    print("...")
    print("Report Sent")

if __name__ == "__main__":
    print(build_report())
    send_report()
```

Run the script and note that the output is the same as before, but now we have the code within functions and the functions being called under `if __name__ == "__main__":`. By changing the script to have this new structure, it will [no longer execute all the lines of code when it is imported](https://realpython.com/if-name-main-python/).

Let's see it in action with the new structure. Change the import statement on `my_module` to point to the new script:

```python
from my_script_with_main import build_report, send_report

def compile_report():
    new_data = [9999]
    imported_data = build_report()
    compiled_data = imported_data + new_data
    print("Now building Compiled Report")
    print(compiled_data)
    print("...")
    print("Now sending Compiled Report")

if __name__ == "__main__":
    compile_report()
```

The output should look like this:

```python
$ python my_module.py
Gathering Data
Building report!
Report Built.
The report is
Now building Compiled Report
[42, 1337, 9999]
...
Now sending Compiled Report
$
```

Note that it all works as intended now. There is no extra report sent because the `send_report()` function was never called from `my_module.py`.

## Conclusion

The main takeaway from this series of examples is to show the difference between a script and a module, and the importance of `if __name__ == "__main__":` even if you don't think your script needs it. You don't know if later on down the road someone will want to import your code and reuse pieces of it, even if it was not originally designed to be imported as a module.

{{</step >}}

<!-- MANDATORY STEP: Call to Action Step is a required step and must be at the end of each codelab -->
{{<step label="Congratulations" duration="1:00" xy-guid="68ed8618-cdad-4ebd-a4b1-23e26a517184">}}

## Learn More

- [DevNet Certifications Community](https://learningnetwork.cisco.com/s/topic/0TO3i0000008jY5GAI/devnet-certifications-community)
- [DevNet Certifications Training Videos](https://learningnetwork.cisco.com/s/devnet-training-videos)
- [Intro to Python&mdash;Cisco Learning Network Free Videos](https://learningnetwork.cisco.com/s/learning-plan-detail-standard?ltui__urlRecordId=a1c6e0000096sAfAAI&ltui__urlRedirect=learning-plan-detail-standard)

{{</step >}}



One of the features in Python that draws in and retains many developers and infrastructure automation engineers is the Python ecosystem of packages. Rather than trying to reinvent the wheel, you can reuse other people's code (or your own old code) to build something new with a few import statements and a few lines of your own to extend the implementation in the direction you need.

What is a Python module? A Python module can be a [few different things](https://realpython.com/python-modules-packages/):

- It can be a Python file with code you want pull in and execute in your own code.
  - This can be either a local file you wrote or a set of code you download and install from a remote source (PyPI) as part of a larger package.
- It can be written in the C programming language and loaded in behind the scenes into Python at run time (like the regular expression module).
- It can be a built-in module included within Python itself (such as the CSV module).
 

## Importing a Built-in Module

To import a built-in module, you need to use the syntax `import MODULE_NAME`. You can include the import statement technically anywhere in your code, though for readability, they are almost always included at the top of your Python file.

Two other examples of a built-in modules are [argparse](https://docs.python.org/3/library/argparse.html#module-argparse), which allows you to make an interactive CLI tool in Python, and [getpass](https://docs.python.org/3/library/getpass.html#module-getpass), which allows you to prompt a user for a password at run time and store it securely (not in plaintext).

When you are developing code, it is good to build things in stages and not try and do it all at once and hope it works. In this example, we will make a CLI tool that prompts the user for a username, password, device type, IP address, and a command to send to the network device. Even though we are not sending actual commands, it is good to get the incremental practice of using these new modules.

When importing a module, you can either use the syntax `import MODULE_NAME`, such as `import argparse`, or you can use the sytnax `from MODULE_NAME import item`. In this case, we will use both styles. The script will start with the import statement `import argparse` and then `from getpass import getpass`. The `getpass` module has a function that is also called `getpass`, so the name appears twice.


{{<step label=" How to Import Local Python Modules" duration="10:00" >}}

Python modules can simply be Python text files that you have locally in your development environment. You can reference your own code and pull it into another Python script to reuse it or extend it. You can import something as small as a single variable, a function, or just import everything to use it in your Python script.

## Importing Variables and Functions from a Module

Let's say you build a quarterly report that gathers CSAT data from your IT Service Management System API, using a list of case numbers given to you. Quarter by quarter, the case numbers will change, but the same logic of getting the CSAT score and plugging that into a CSV file for management to review will stay the same. You can use the CSV built-in library to build the report and abstract the functions that gather the CSAT score and build the report into a separate module.

Create a Python file called `shared_resources.py` with the following contents:

```python
import random, csv

def lookup_itsm_csat(case_number):
    print("making API call to IT Service Management System for case {}".format(str(case_number)))
    print("Gathering CSAT Score")
    return random.randint(0, 5)

def build_csv_report(case_numbers, csat_list, region, year, quarter):
    csv_file = "csat_report_fy{}q{}_{}.csv".format(str(year), str(quarter), region)
    try:
        with open(csv_file, "w") as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=["case_number", "csat"]
            )
            writer.writeheader()
            # this could be written in a loop, but writing this way for simplicity
            writer.writerow({'case_number': case_numbers[0], 'csat': csat_list[0]})
            writer.writerow({'case_number': case_numbers[1], 'csat': csat_list[1]})
            writer.writerow({'case_number': case_numbers[2], 'csat': csat_list[2]})
            writer.writerow({'case_number': case_numbers[3], 'csat': csat_list[3]})
    except IOError:
        print("I/O error")
```

This Python module uses the random standard library to make a fake CSAT score and has a function to write out the CSAT with the case numbers into a CSV file. You could do a bit more massaging of the code to have it loop over the rows, but I am keeping it explicit and simple here because we are just teaching about importing modules.

Now create another file to import that module, calling it `FYXX_Q4_BUILD_REPORT.py` in the same working directory with the following contents:

```python
#!/usr/bin/python3
from shared_resources import lookup_itsm_csat, build_csv_report

if __name__ == "__main__":
    csat_list = []
    case_numbers = [1241, 1234, 6453, 3453]
    print("building report")
    print("looking up CSAT scores using API for case numbers in IT Service Management System")
    for case_num in case_numbers:
        # add csat to dictionary for case number 
        csat = lookup_itsm_csat(case_num)
        csat_list.append(csat)
        print("csat for {} is {}".format(str(case_num), str(csat)))
    build_csv_report(case_numbers=case_numbers, csat_list=csat_list, region="emea", year="2023", quarter="4")

```

This script imports the two functions from the `shared_resources` Python module, plugging in case numbers and other minor details that are used to generate the CSV filename.

The output should look something like this (with other numbers for CSAT because they are randomly generated):

```python
$ python FYXX_Q4_BUILD_REPORT.py
building report
looking up CSAT scores using API for case numbers in IT Service Management System
making API call to IT Service Management System for case 1241
Gathering CSAT Score
csat for 1241 is 3
making API call to IT Service Management System for case 1234
Gathering CSAT Score
csat for 1234 is 2
making API call to IT Service Management System for case 6453
Gathering CSAT Score
csat for 6453 is 5
making API call to IT Service Management System for case 3453
Gathering CSAT Score
csat for 3453 is 1
$
$ cat csat_report_fy2023q4_emea.csv
case_number,csat
1241,3
1234,2
6453,5
3453,1
$
```

### One Last Thing

In Python, it [searches for new modules](https://realpython.com/python-modules-packages/#the-module-search-path) first in your current working directory, and then in your `PYTHONPATH` environmental variable, and then in any other places you might have configured Python to look. Most of the time, you are going to have your Python modules in your current working directory, or in a subdirectory, or installed from pip. This tutorial was focused on getting you started with some practical examples of importing modules, but there is much more to learn when it comes to Python pathing and managing your Python modules. For most beginners, though, you will not have to worry about it.

{{</step >}}

<!-- MANDATORY STEP: Call to Action Step is a required step and must be at the end of each codelab -->
{{<step label="Congratulations" duration="1:00" >}}

## Learn More

- [DevNet Certifications Community](https://learningnetwork.cisco.com/s/topic/0TO3i0000008jY5GAI/devnet-certifications-community)
- [DevNet Certifications Training Videos](https://learningnetwork.cisco.com/s/devnet-training-videos)
- [Intro to Python&mdash;Cisco Learning Network Free Videos](https://learningnetwork.cisco.com/s/learning-plan-detail-standard?ltui__urlRecordId=a1c6e0000096sAfAAI&ltui__urlRedirect=learning-plan-detail-standard)

{{</step >}}

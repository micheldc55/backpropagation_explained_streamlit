import streamlit
import typing

def wrapper_html_tags(config: str, html_tag_type: str = "p") -> typing.Tuple[str, str]:
    """Function that generates the left and right wrappers for an HTML tag.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    :return: Returns a tuple of the left and right wrappers around the text.
    :rtype: typing.Tuple[str, str]
    """
    wrapper_left = f"<{html_tag_type} {config}>"
    wrapper_right = f"</{html_tag_type}>"
    return wrapper_left, wrapper_right

def wrap_text_markdown(text: str, config: str, html_tag_type: str = "p") -> str:
    """Function that takes a text and a the HTML attributes and returns the string to place
    in a markdown streamlit cell.

    :param text: Text to be used in the HTML tag.
    :type text: str
    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    :return: Returns the text wrapped in its markdown tags and attributes.
    :rtype: str
    """
    wrapper_left, wrapper_right = wrapper_html_tags(config, html_tag_type)
    markdown = f"{wrapper_left}{text}{wrapper_right}"
    return markdown

def introduction_text_paragraph1(config: str, html_tag_type: str = "p") -> tuple:
    """Generates the text that will be used in the introduction.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """If you have studied Deep Learning or are interested in the subject, you've probably come across 
    the terms <b>backpropagation</b> and <b>gradient descent</b>. If you've been paying attention to the scene you probably 
    even heard some more mathematical terms like <b>matrix multiplications</b> or even the <b>Chain Rule</b>. We've all heard about 
    them at some point during our journey, but do we understand how they are used in Neural Networks? I certainly didn't,
    and that's why I'm building this small streamlit app that will walk you through some of this concepts and their 
    applications!"""

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def introduction_text_paragraph2(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used in the introduction.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """

    text = """In this short introduction to <b>backpropagation for Deep Learning applications</b>, we will mostly follow 
    <a href="https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ">Andrej Karpathy's 
    video</a> on the topic, and add a few extra comments here and there that give my own perspective on the subject 
    or help clarify something that I didn't understand when going through his material. To be clear, everyone looking 
    at this dashboard should definitely go and check out his content, as he is both the developer of the <b>micrograd</b> 
    library, and the person from whom I took the idea to build this dashboard."""

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def introduction_getting_started1(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used in the getting started section.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """

    text = """You will be able to interact with most of the elements used in this tutorial to test and get a sense of how 
    backpropagation works. We will be using <b>micrograd</b> (link to the github repository <a href="">here</a>) a library that 
    aims to show how backpropagation works on a simplified level. The simplified doesn't mean that micrograd cuts corners, 
    quite the opposite! You will notice that with this simple library (I encourage you to check the documentation and the 
    code length) we can implement backpropagation for any deep learning network. """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def parabola_introduction1(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for explaining what a parabola is.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Let's start simple. Let's introduce the function that we are going to be using during this introductory tutorial: 
    The <b>Parabola</b>. The parabola is a quadratic function defined by three parameters <b>a</b>, <b>b</b> and <b>c</b>. 
    These parameters define some characteristics of the parabola. The "a" determines the concavity of the parabola (if it's 
    happy or sad), the "b" parameter moves the parabola around (you won't be able to see it in the plot) and the "c" parameter moves 
    the parabola up and down and changes the place where the parabola intersects the x axis. The general formula of the parabola is:
    <br>
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def parabola_introduction2(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for explaining what a parabola is.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """In the next section, we will introduce the concept of <b>derivatives</b> so understanding what a parabola is
    will come in handy. In the figure above we se the general equation of a parabola in terms of its parameters "a", "b" and 
    "c". The function transforms the value of the variable x, to a value f(x) as shown in the title of the plot, using these 
    three parameters (a, b and c). Below, you can play around with the sliders to change the value of the parameters, and 
    see how they affect the shape of the parabola.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def parabola_subtext(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be placed below the parabola plot from echarts.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """This tutorial will mostly use the Apache Echarts library. So if you like the visuals be sure to check the library out!
    This library is written in Javascript, so it may be helpful to be somewhat familiar with the language! If you have never used 
    Echarts, I strongly recommend giving it a go, especially if you need interactive plots. More on the library 
    <a href="https://echarts.apache.org/en/index.html">here</a>. They can be easily integrated with streamlit using the 
    st_echarts library as well!
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def derivatives_intro1(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for explaining what a derivative is.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """This section introduces the concept of derivatives. In mathematics, a derivative of a function at a given point x is given 
    by the ratio of the difference between the function evaluated at x and at an infinitesimal increment of the same function, divided 
    by the increment in the dependent variable, when the increment tends to zero. But what is all this jargon?
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def derivatives_intro2(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for explaining what a derivative is.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """The truth is that derivatives are much harder to put into words mathematically than they are to explain in simple terms.
    Basically, the derivative of a function at x measures the slope of a line tangential to the function at that point. It shows us what 
    would happen to the value of the function if we incremented x by a tiny bit. This number is generally represented with the letter 
    "h" and so the definition of the derivative could be expressed mathematically like this:
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def derivatives_mathematically1(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for explaining what a derivative is.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Let's get to the value of a derivative analitically, so that we can see what effort it would take to implement it in code.
    To do so, let's imagine we have a function, as shown below, and we want to calculate the derivative of the function. We will do it 
    in a generic way, and then evaluate at a point of our choice, say x=1.5.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def derivatives_mathematically1(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for explaining what a derivative is.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """This equation is read in the following way: The derivative of the function f with respect to the variable 
    x is the limit of the ratio between the difference of the function evaluated at x + h and the function evaluated at x, 
    normalized by the increment "h", when "h" gets smaller and smaller.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def right_of_plot_text(config: str, html_tag_type: str = "ul", dict_params: dict = {}) -> str:
    """Generates the text that will be displayed to the right of the derivative plot.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    h = dict_params.get("h")
    x = dict_params.get('x')
    slope = dict_params.get('slope')
    actual_slope = 2*x
    if actual_slope == 0:
        ratio = slope * 100
    else:
        ratio = (slope/actual_slope - 1) * 100
    percent_diff_slopes = round(ratio, 3) 

    if percent_diff_slopes < 0.05:
        percent_diff_slopes = '> 0.05'

    text = f"""<li>The value of the numerically approximated slope in this case is: <b>{slope}</b></li>
    <li>The actual value of the derivative at x={x} is: <b>{actual_slope}</b></li>
    <li>With h={h} the percentage differece between the numerical (approximated) slope and the derivative is: <b>{percent_diff_slopes}%</b></li>
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def deriving_derivatives_by_hand(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for explaining what a derivative is.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Now, notice that this definition is independent of any function we use. As long as the limit exists and is unique, 
    we will say the function has a derivative. The way we would solve this mathematically is by calculating the limit in the 
    definition of a derivative at a point of interest (x). The problem with this is that it is not always trivial to calculate 
    that limit. Let's show a simple example to understand why even in a simple example this is not trivial. Feel free to ignore 
    this if you are not interested in the mathematics behind derivatives! <br><br>
    Let's calculate the derivative at x = -1 for the function f(x) = x^2 + 1. If we check online, we will find out that the 
    derivative is equals 2x, but we want to get to that results through the definition:
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def derivatives_numerical(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for numerically approximating a derivative.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Now, the process of calculating a derivative is very elegant and mathematically sound. But it also needs the user to 
    be mathematically savvy to use that definition. For each function, we would need to derive the correct expression for the derivative 
    and hard-code it into our process. 
    <br><br>But what if I told you that you can get a very good approximation using a few lines 
    of code? This method would be an estimation of course, but it would make deriving complex functions easy. Let's see how we can 
    implement this!
    <br><br>Let's implement this by looking at the definition of the derivative. If we take the definition shown above, we can write an 
    approximate version of it using the following process. In our definition, <b>h</b> is an infinitesimal increment (this is jargon 
    for a very very small step). But what if we change the "infinitesimal" increment concept and substitute it by a very small, but real 
    increment?
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown    

def derivatives_math_example(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for numerically approximating a derivative.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Let's run this process with a function we know well from the steps we took above... The x<sup>2</sup> + 1 function. 
    The slope of the function at a point "p" is equal to 2p, as we have derived above. So let's calculate the numerical 
    approximation of the derivative and compare the results.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def derivatives_numerical_example(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be used for numerically approximating a derivative.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Let's approximate the derivative of the function using h = 0.001. This will be an approximate result, but we will see 
    that even using this simple approach, we get a very good result for the derivative. To derive this approximation, we start 
    by using the definition of a derivative, and selecting a small number for h, as state above.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def top_of_parabola_derivative_text(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will be shown above the parabolas. This explains how to use the widgets.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """We are now going to test this concepts we learned on the same function we've been using. But now 
    we will be able to play around with the value of h, and also we will be able to select different points in 
    which to approximate the derivative. In the summary below, you will get the real value of the derivative 
    at the selected point, the approximated value, and the percentage difference, calculated as 
    (approximated slope - real slope) / approximated slope. <br><br>
    Try moving some values around and try to <b>predict</b> what will happen to the values of the <b>approximated 
    derivative</b> as the value of h decreases.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def chain_rule_definition(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will define the chain rule.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Let's imagine we have a function "y", which depends on a variable "u". So we can write <b>y = f(u)</b> in mathematical 
    notation. This means that the function "y" changes when "u" changes, through a given function f. So, if f(u) = 2u, it means 
    that for every change in 1 unit of u, y grows by 2. For our use case, this function f can be any differentiable function 
    you can think of. It is not the purpose of this tutorial, but you can find what being differentiable means 
    <a href="https://www.mathsisfun.com/calculus/differentiable.html#:~:text=Differentiable%20means%20that%20the%20derivative%20exists...%20Example%3A%20is,exist%20for%20every%20value%20in%20the%20function%27s%20domain.">
    here</a>, but it basically means that the derivative of the function <b>exists</b>.<br><br>
    Now what would happen if that function u depended on another variable "x"? We can also calculate the derivative of u with 
    respect to x, using the limit definition we saw before. But how could we calculate the impact that slightly changing x has on 
    the original function "y"? That's were the <b>chain rule comes in handy</b>. In simple terms, the chain rule states that if 
    the rate of change of u with respect to x is 2, and the rate of change of y with respect to u is 4, then the rate of change 
    of y with respect to x is the <b>product</b> of the two, so <b>8</b>. In <b>mathematical jargon</b>, this is written like below, but 
    the concept is the same!<br><br>
    The <b>only</b> thing you need to know for the next section is that if y = 4u, then the derivative of y with respect to u (dy/du) is 4. 
    And if u = 2x, then the derivative of u with respect to x (du/dx) is 2.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def chain_rule_applied_to_backprop(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will define the chain rule.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """There is a lot of mathematics that we are skipping here, but the steps mentioned above are all you need to understand 
    the chain rule for Neural Networks and Backpropagation. In my opinion, this is all you need to know to gain a basic 
    understanding of how Backpropagation works, except for a small detail that we'll go over in the next page. But first, the short quiz 
    below will help you identify if you need to go back to any section for a refresher of any of the concepts we have discussed here!
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def button_explanation_take_test(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will explain how to use the Test Button

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """Choose the correct answer for the questions shown in the multiple choice below (there is only one correct answer). 
    Once you have selected what you believe to be the correct answers, go to the bottom of the page and click on the "Check Answers" 
    button.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def intro_test_question1(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will explain how to use the Test Button

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """<b>Question 1:</b> Suppose we have a function F = f(y), where function y = g(x). This means that F is a function of "y" 
    and "y" is a different function of "x". When is the Chain Rule applicable?
    <ul>
        <li>1) When solving a Machine Learning problem only.</li>
        <li>2) If x, y, F and g exist.</li>
        <li>3) If dF/dy and dy/dx exist.</li>
        <li>4) Only if F and y are parabolas.</li>
    </ul>
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown

def intro_test_question2(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will explain how to use the Test Button

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """<b>Question 2:</b> Suppose we want to make a function that depends on "x" to <b>decrease</b> in value? 
    Assume we know the derivative of f with respect to x at the point we are interested in exists and is: df/dx = -3. Should we increase 
    or decrease the value of x?
    <ul>
        <li>1) If you increase x, f(x) will decrease.</li>
        <li>2) If you decrease x, f(x) will decrease.</li>
        <li>3) We don't know if the function is differentiable.</li>
        <li>4) We need more data.</li>
    </ul>
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def intro_test_question3(config: str, html_tag_type: str = "p") -> str:
    """Generates the text that will explain how to use the Test Button

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    text = """<b>Question 3:</b> Using the graphical visualization in the "Derivatives" page, can you guess where the minimum 
    value of the function x^2 + 1 is reached? What is the value of the derivative at this point? Try to guess it by looking 
    at how the slope will be when "h" gets infinitely small!
    <ul>
        <li>1) The <b>minimum</b> value of x^2 + 1 is reached in x=0, and the value of the <b>derivative</b> is 2.</li>
        <li>2) The <b>minimum</b> value of x^2 + 1 is reached in x=0, and the value of the <b>derivative</b> is 0.</li>
        <li>3) The <b>minimum</b> value of x^2 + 1 is reached in x=-1, and the value of the <b>derivative</b> is 0.</li>
        <li>4) The <b>minimum</b> value of x^2 + 1 is reached in x=0, and the value of the <b>derivative</b> is -2.</li>
    </ul>
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def answer_question1_intro(config: str, html_tag_type: str = "p", is_correct: bool = False) -> str:
    """Generates the text that will explain the answer to question 1 of the inroduction.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    if is_correct:
        status = 'Correct!'
    else:
        status = "Whoops! That's not the correct answer!"
    text = f"""<br>{status} The correct answer is number 3! In order for us to apply the chain rule, the function has 
    to be differentiable at the point we want to calculate it.<br>
    Number 2 is not the case, because a function can exist but not be differentiable, you can read a lot more about it 
    <a href="https://www.statisticshowto.com/derivatives/differentiable-non-functions/">here</a>.<br>
    Number 4 is wrong because of the word <b>only</b>. Parabolas are differentiable, but so are a plethora of other functions.
    <br>Finally, number 1 is a common misconception that probably stems from not having a pure mathematical background, and it 
    is that this is not only applicable to Machine Learning. A lot of traditional optimization problems use this same concepts!
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def answer_question2_intro(config: str, html_tag_type: str = "p", is_correct: bool = False) -> str:
    """Generates the text that will explain the answer to question 1 of the inroduction.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    if is_correct:
        status = 'Correct!'
    else:
        status = "Whoops! That's not the correct answer!"
    text = f"""<br><br><br>{status} The correct answer is number 1! The function has a negative slope at the point we are looking 
    at. This means that if we increase x by a small amount, the function will go down in value.<br>
    Number 2 is not the case, because it states exactly the opposite.<br>
    Number 3 is wrong because we know from the problem statement that the derivative exists at "x", therefore, it's differentiable.
    <br>Finally, number 4 is wrong because we have all the information needed to decide. The derivative exists, so the function is 
    differentiable, and we know the value of the derivative which says what happend with f(x) if we increase x by a tiny amount.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown


def answer_question3_intro(config: str, html_tag_type: str = "p", is_correct: bool = False) -> str:
    """Generates the text that will explain the answer to question 1 of the inroduction.

    :param config: The attributes of the html tag. If it is a string, it will be something 
    like: style="font-family:Courier; color:Blue; font-size: 20px;"
    :type config: str
    :param html_tag_type: HTML name of the tag, for example table, p, h1, etc. Defaults to "p"
    :type html_tag_type: str, optional
    """
    if is_correct:
        status = 'Correct!'
    else:
        status = "Whoops! That's not the correct answer!"
    text = f"""<br><br><br><br>{status} The correct answer is number 2! The minimum value of a function is reached when 
    the value of the derivative is <b>zero</b>. In Deep Learning, we generally want to minimize a loss function, so we 
    will be moving in the direction that reduces the value of the function.<br>
    Number 1 is wrong, the minimum value is 0, but the derivative at that point is not 2. Check the interactive plot to verify!<br>
    Number 3 is wrong, the minimum value is not -1, as you can see directly in the plot.
    <br>Finally, number 4 is wrong because the derivative at 0 is not -2.
    """

    markdown = wrap_text_markdown(text, config, html_tag_type)

    return markdown
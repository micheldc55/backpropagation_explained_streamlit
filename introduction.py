import streamlit
from streamlit_echarts import st_echarts
import numpy as np
import matplotlib.pyplot as plt
from micrograd.engine import Value
import long_texts, table_of_contents
import plotting_functions
import math_in_latex

def create_intro_page(sidebar):
    """Creates the introduction page. Takes a streamlit sidebar as input.

    :param sidebar: Streamlit sidebar
    :type sidebar: streamlit.sidebar
    """
    sidebar.markdown('<h1>Table of Contents:</h1>', unsafe_allow_html=True)

    toc = table_of_contents.TableOfContents()
    toc.placeholder(sidebar=True)

    streamlit.markdown('<h1 style="font-size: 38px;">Introduction to Backpropagation<br></h1>', unsafe_allow_html=True)
    streamlit.markdown('<h2 style="font-size: 30px;">Fundamentals for Deep Learning applications<br><br></h2>', unsafe_allow_html=True)

    streamlit.markdown('<img src="https://garudacyber.co.id/an-component/media/upload-gambar-artikel/backpropagation.jpg" alt="drawing" width="600"/>', unsafe_allow_html=True)
    streamlit.write('Image taken from [this page](https://garudacyber.co.id/artikel/635-logika-dan-algoritma-backpropagation)')

    #### INTRODUCTION ####
    toc.subheader("Introduction", font_size=24)
    # streamlit.markdown('<h3 style="font-size: 24px;">Introduction</h3>', unsafe_allow_html=True)
    intro_col1, _ = streamlit.columns([4, 1])

    intro_markdown_p1 = long_texts.introduction_text_paragraph1(config='style="font-size: 18px;"', html_tag_type = "p")
    intro_col1.markdown(intro_markdown_p1, unsafe_allow_html=True)

    intro_markdown_p2 = long_texts.introduction_text_paragraph2(config='style="font-size: 18px;"', html_tag_type = "p")
    intro_col1.markdown(intro_markdown_p2, unsafe_allow_html=True)

    #### GETTING STARTED ####
    toc.subheader("Getting Started", font_size=24)
    # streamlit.markdown('<h3 style="font-size: 24px;">Getting Started</h3>', unsafe_allow_html=True)
    get_star_col1, _ = streamlit.columns([4, 1])

    gs_markdown_p1 = long_texts.introduction_getting_started1(config='style="font-size: 18px;"', html_tag_type = "p")
    get_star_col1.markdown(gs_markdown_p1, unsafe_allow_html=True)

    parabola_p1 = long_texts.parabola_introduction1(config='style="font-size: 18px;"', html_tag_type = "p")
    get_star_col1.markdown(parabola_p1, unsafe_allow_html=True)

    streamlit.markdown('<img src="https://www.mechamath.com/wp-content/uploads/2021/08/vertex-of-a-parabola-in-standard-form.png" alt="drawing" width="200"/>', unsafe_allow_html=True)
    streamlit.write('Image taken from [this page](https://www.mechamath.com/wp-content/uploads/2021/08/vertex-of-a-parabola-in-standard-form.png)')
    
    get_star_col2, _ = streamlit.columns([4, 1])
    parabola_p2 = long_texts.parabola_introduction2(config='style="font-size: 18px;"', html_tag_type = "p")
    get_star_col2.markdown(parabola_p2, unsafe_allow_html=True)

    # E-Chart
    slider_col, non_slider_col = streamlit.columns([3, 6])
    a = slider_col.slider('Change the "a" parameter of the parabola below:', -4., 4., step=0.25)
    b = slider_col.slider('Change the "b" parameter of the parabola below:', -4., 4., step=0.25)
    c = slider_col.slider('Change the "c" parameter of the parabola below:', -4., 4., step=0.25)

    x_values = np.array([value for value in np.arange(-2, 2, 0.25)])

    plotting_functions.plot_interactive_parabola(x_values, a, b, c)

    parabola_substring_col, _ = streamlit.columns([4, 1])
    parabola_substring = long_texts.parabola_subtext(config='style="font-size: 18px;"', html_tag_type = "p")
    parabola_substring_col.markdown(parabola_substring, unsafe_allow_html=True)

    toc.generate()




def create_derivatives_page(sidebar = None):
    """Creates the derivatives page. Takes a streamlit sidebar as input.

    :param sidebar: Streamlit sidebar object to be passed if you need a sidebar with content.
    :type sidebar: sidebar or None
    """
    if sidebar is None:
        sidebar = streamlit.sidebar()

    sidebar.markdown('<h1>Table of Contents:</h1>', unsafe_allow_html=True)

    toc = table_of_contents.TableOfContents()
    toc.placeholder(sidebar=True)

    streamlit.markdown('<h1 style="font-size: 38px;">Introduction to Derivatives<br></h1>', unsafe_allow_html=True)
    streamlit.markdown('<h2 style="font-size: 30px;">How they work and how they connect to Deep Learning<br><br></h2>', unsafe_allow_html=True)

    toc.header("The concept behind a derivative", font_size=24)

    intro_col1, _ = streamlit.columns([4, 1])

    derivatives1 = long_texts.derivatives_intro1(config='style="font-size: 18px;"', html_tag_type = "p")
    intro_col1.markdown(derivatives1, unsafe_allow_html=True)

    derivatives2 = long_texts.derivatives_intro2(config='style="font-size: 18px;"', html_tag_type = "p")
    intro_col1.markdown(derivatives2, unsafe_allow_html=True)

    # LaTeX equation --> definition of derivative:
    math_in_latex.write_derivative_definition_latex(intro_col1)

    derivatives_math1 = long_texts.derivatives_mathematically1(config='style="font-size: 18px;"', html_tag_type = "p")
    intro_col1.markdown(derivatives_math1, unsafe_allow_html=True)

    intro_col1.markdown('<img src="https://www.mathwarehouse.com/calculus/derivatives/images/graph2-derivative-increasing-decreasing.png" alt="drawing" width="600"/>', unsafe_allow_html=True)
    intro_col1.write('Image taken from [this page](https://www.mathwarehouse.com/calculus/derivatives/images/graph2-derivative-increasing-decreasing.png)')

    toc.header('Calculating the derivative, the boring but precise way...', font_size=24)

    derivative_math_behind_col, _ = streamlit.columns([4, 1])

    derivative_math_behind = long_texts.deriving_derivatives_by_hand(config='style="font-size: 18px;"', html_tag_type = "p")
    derivative_math_behind_col.markdown(derivative_math_behind, unsafe_allow_html=True)

    # LaTeX equations for deriving the derivative of x^2 + 1
    math_in_latex.derive_example_derivative()

    toc.header('Calculating the derivative numerically', font_size=24)

    derivative_math_col, _ = streamlit.columns([4, 1])

    derivatives_numerical = long_texts.derivatives_numerical(config='style="font-size: 18px;"', html_tag_type = "p")
    derivative_math_col.markdown(derivatives_numerical, unsafe_allow_html=True)

    math_in_latex.write_numerical_approximation_derivate(derivative_math_col)
    derivative_math_col.write('\n')

    toc.subheader('Mathematical derivative', font_size=20)

    numerical_vs_math_derivative_col, _ = streamlit.columns([4, 1])

    derivatives_numerical2 = long_texts.derivatives_math_example(config='style="font-size: 18px;"', html_tag_type = "p")
    numerical_vs_math_derivative_col.markdown(derivatives_numerical2, unsafe_allow_html=True)
    
    math_in_latex.compare_num_derivative_vs_math_derivative__math_derivative(numerical_vs_math_derivative_col)
    numerical_vs_math_derivative_col.write('\n')

    toc.subheader('Numerical approximation', font_size=20)

    numerical_vs_math_derivative_col2, _ = streamlit.columns([4, 1])

    derivatives_numerical3 = long_texts.derivatives_numerical_example(config='style="font-size: 18px;"', html_tag_type = "p")
    numerical_vs_math_derivative_col2.markdown(derivatives_numerical3, unsafe_allow_html=True)
    math_in_latex.compare_num_derivative_vs_math_derivative__num_derivative(numerical_vs_math_derivative_col2)
    numerical_vs_math_derivative_col2.write('\n')

    derivatives_numerical4 = long_texts.top_of_parabola_derivative_text(config='style="font-size: 18px;"', html_tag_type = "p")
    numerical_vs_math_derivative_col2.markdown(derivatives_numerical4, unsafe_allow_html=True)
    
    
    parabola_plot_col, _, right_of_plot_col = streamlit.columns([2, 1, 3])

    x = parabola_plot_col.radio(
        'Select the point (x) in which you want to evaluate the derivative of f(x):',
        [-1, 0, 0.5, 1],
        index=3
    )
    h = parabola_plot_col.select_slider(
        'Change the value of h. The smaller the value of h the more precise the derivative will be',
        [10., 5., 1., 0.5, 0.1, 0.05, 0.01, 0.001, 0.0001]
    )
    plotting_functions.plot_parabola_for_concept_of_derivative(x=x, h=h)

    inputs  = np.array([x, x+h])
    outputs = plotting_functions.test_parabola(inputs)
    x1, x2, y1, y2 = (inputs[0], inputs[1], outputs[0], outputs[1])

    dict_params = {'h': h, 'x': x, 'slope': (y2 - y1)/(x2 - x1)}
    right_of_plot_text = long_texts.right_of_plot_text(config='style="font-size: 18px;"', html_tag_type = "ul", dict_params=dict_params)
    streamlit.markdown(right_of_plot_text, unsafe_allow_html=True)

    toc.generate()




def create_chain_rule_page(sidebar):
    """Creates the derivatives page. Takes a streamlit sidebar as input.

    :param sidebar: Streamlit sidebar object to be passed if you need a sidebar with content.
    :type sidebar: sidebar or None
    """
    if sidebar is None:
        sidebar = streamlit.sidebar()

    sidebar.markdown('<h1>Table of Contents:</h1>', unsafe_allow_html=True)

    toc = table_of_contents.TableOfContents()
    toc.placeholder(sidebar=True)

    streamlit.markdown('<h1 style="font-size: 38px;">The Chain Rule<br></h1>', unsafe_allow_html=True)
    streamlit.markdown('<h2 style="font-size: 30px;">A soft introduction to the Chain Rule and its use in Deep Learning<br><br></h2>', unsafe_allow_html=True)

    intro_col1, _ = streamlit.columns([4, 1])

    intro_col1.markdown('<img src="https://cdn1.byjus.com/wp-content/uploads/2021/03/Chain-rule-formula.png" alt="drawing" width="300"/>', unsafe_allow_html=True)
    intro_col1.write('Image taken from [this page](https://cdn1.byjus.com/wp-content/uploads/2021/03/Chain-rule-formula.png)')

    streamlit.write('\n')

    toc.header("Defining the Chain Rule", font_size=24)

    definition_col1, _ = streamlit.columns([4, 1])

    chain_rule_def = long_texts.chain_rule_definition(config='style="font-size: 18px;"', html_tag_type = "p")
    definition_col1.markdown(chain_rule_def, unsafe_allow_html=True)
    
    math_in_latex.chain_rule_definition_and_example(definition_col1)
    definition_col1.write('\n')

    chain_rule_application = long_texts.chain_rule_applied_to_backprop(config='style="font-size: 18px;"', html_tag_type = "p")
    definition_col1.markdown(chain_rule_application, unsafe_allow_html=True)

    toc.header("Test time!", font_size=24)
    
    test_col1, _ = streamlit.columns([4, 1])
    
    test_introduction = long_texts.button_explanation_take_test(config='style="font-size: 18px;"', html_tag_type = "p")
    test_col1.markdown(test_introduction, unsafe_allow_html=True)

    answers_col1, answers_col2 = streamlit.columns([3, 3])

    question1 = long_texts.intro_test_question1(config='style="font-size: 18px;"', html_tag_type = "p")
    answers_col1.markdown(question1, unsafe_allow_html=True)

    answer1 = answers_col1.selectbox('You selected:', (1, 2, 3, 4), key='q1')

    question2 = long_texts.intro_test_question2(config='style="font-size: 18px;"', html_tag_type = "p")
    answers_col1.markdown(question2, unsafe_allow_html=True)

    answer2 = answers_col1.selectbox('You selected:', (1, 2, 3, 4), key='q2')

    question3 = long_texts.intro_test_question3(config='style="font-size: 18px;"', html_tag_type = "p")
    answers_col1.markdown(question3, unsafe_allow_html=True)

    answer3 = answers_col1.selectbox('You selected:', (1, 2, 3, 4), key='q3')

    show_answers = answers_col1.button('Check Answers')
    if show_answers:
        if answer1 != 3:
            answer_q1 = long_texts.answer_question1_intro(
                config='style="font-size: 18px;color:Tomato;"', html_tag_type = "p", is_correct=False
            )
            answers_col2.markdown(answer_q1, unsafe_allow_html=True)
        else:
            answer_q1 = long_texts.answer_question1_intro(
                config='style="font-size: 18px;color:MediumSeaGreen;"', html_tag_type = "p", is_correct=True
            )
            answers_col2.markdown(answer_q1, unsafe_allow_html=True)
        
        if answer2 != 1:
            answer_q2 = long_texts.answer_question2_intro(
                config='style="font-size: 18px;color:Tomato;"', html_tag_type = "p", is_correct=False
            )
            answers_col2.markdown(answer_q2, unsafe_allow_html=True)
        else:
            answer_q2 = long_texts.answer_question2_intro(
                config='style="font-size: 18px;color:MediumSeaGreen;"', html_tag_type = "p", is_correct=True
            )
            answers_col2.markdown(answer_q2, unsafe_allow_html=True)

        if answer3 != 1:
            answer_q3 = long_texts.answer_question3_intro(
                config='style="font-size: 18px;color:Tomato;"', html_tag_type = "p", is_correct=False
            )
            answers_col2.markdown(answer_q3, unsafe_allow_html=True)
        else:
            answer_q3 = long_texts.answer_question3_intro(
                config='style="font-size: 18px;color:MediumSeaGreen;"', html_tag_type = "p", is_correct=True
            )
            answers_col2.markdown(answer_q3, unsafe_allow_html=True)

    toc.generate()


def create_max_min_concept_derivatives(sidebar):
    """Creates the Min/Max page. Takes a streamlit sidebar as input.

    :param sidebar: Streamlit sidebar object to be passed if you need a sidebar with content.
    :type sidebar: sidebar or None
    """
    if sidebar is None:
        sidebar = streamlit.sidebar()

    sidebar.markdown('<h1>Table of Contents:</h1>', unsafe_allow_html=True)

    toc = table_of_contents.TableOfContents()
    toc.placeholder(sidebar=True)

    streamlit.markdown('<h1 style="font-size: 38px;">Why is all this preface important?<br></h1>', unsafe_allow_html=True)
    streamlit.markdown('<h2 style="font-size: 30px;">Minimizing/Maximizing functions --> The concept behind optimization<br><br></h2>', unsafe_allow_html=True)

    intro_col1, _ = streamlit.columns([4, 1])

    intro_col1.markdown('<img src="https://th.bing.com/th/id/R.b7ceef4024954b4c6114d35ced6d224d?rik=LZVmxW%2fvXa%2f4NA&riu=http%3a%2f%2fwww.ccl.net%2fcca%2fdocuments%2fmolecular-modeling%2ffig22.gif&ehk=8Xupt8dReZ8LXwOHcwcP0Md2jKFo3W%2fyR4Ey37R6eio%3d&risl=&pid=ImgRaw&r=0" alt="drawing" width="500"/>', unsafe_allow_html=True)
    intro_col1.write('Image taken from [this page](http://www.ccl.net/cca/documents/molecular-modeling/node8.html)')

    streamlit.write('\n')

    toc.header("Defining the Chain Rule", font_size=24)
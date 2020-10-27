from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from user_pass import mail_pass
from datetime import date
import calendar
from pdb import set_trace

def get_day():
    today = date.today()
    current_day = calendar.day_name[today.weekday()]
    return current_day

def multiple_selection(option):
    driver.find_element_by_xpath(option).click()

email, password = mail_pass()

chromedriver_location = r"C:\Users\Elias\Desktop\Elias\chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://dashboard.microverse.org/login')

same_form_days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
notice = "*" * 15
current_day = get_day()
mail_input = '//*[@id="1-email"]'
password_input = '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/input'
login_button = '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button'
week_back_button = '//*[@id="app"]/div/main/div/div/div[14]/div[1]/div/a'
monday_standup = '#app > div > main > div > div > div.row.no-gutters.mt-2 > div > div.row.no-gutters.mt-2.mb-2.standup-blocks > div:nth-child(1) > button'
tuesday_standup = '#app > div > main > div > div > div.row.no-gutters.mt-2 > div > div.row.no-gutters.mt-2.mb-2.standup-blocks > div:nth-child(2) > button'
wednesday_standup = '#app > div > main > div > div > div.row.no-gutters.mt-2 > div > div.row.no-gutters.mt-2.mb-2.standup-blocks > div:nth-child(3) > button'
thursday_standup = '#app > div > main > div > div > div.row.no-gutters.mt-2 > div > div.row.no-gutters.mt-2.mb-2.standup-blocks > div:nth-child(4) > button'
friday_standup = '#app > div > main > div > div > div.row.no-gutters.mt-2 > div > div.row.no-gutters.mt-2.mb-2.standup-blocks > div.pb-3.pt-3.col.dashboard-daily-info-boxes.text-center.retrospective-blocks > button'

# Mon-Thur form buttons
achieved_goals = '//*[@id="standup_achieved_goals"]'
went_well = '//*[@id="standup_upsides"]'
nothing_wrong = '//*[@id="blockers_none"]'
goal1 = '//*[@id="goals_1"]'
goal2 = '//*[@id="goals_2"]'
goal3 = '//*[@id="goals_3"]'
rest = '//*[@id="standup_goals_confidence"]'
happy_face = '//*[@id="motivation_0"]'
submit = '//*[@id="new_standup"]/div[2]/input'

# Fri form buttons
friday_achieved_goals = '//*[@id="retrospective_goal_achievement"]'
friday_nothing_wrong = '//*[@id="retrospective_blockers_none"]'
friday_went_well = '//*[@id="retrospective_upsides"]'
friday_goal1 = '//*[@id="retrospective_goals_1"]'
friday_goal2 = '//*[@id="retrospective_goals_2"]'
friday_goal3 = '//*[@id="retrospective_goals_3"]'
friday_rest = '//*[@id="retrospective_action_items"]'
friday_happy_face = '//*[@id="motivation_0"]'
friday_submit = '//*[@id="new_standup"]/div[2]/input'
faster = '//*[@id="retrospective_partner_learn_style_feedback_a_faster_learner"]'
experienced = '//*[@id="retrospective_partner_learn_style_feedback_too_experienced"]'
punctual = '//*[@id="retrospective_partner_learn_style_feedback_punctual"]'
good_com = '//*[@id="retrospective_partner_learn_style_feedback_a_good_communicator"]'
great_collab = '//*[@id="retrospective_partner_learn_style_feedback_a_great_collaborator"]'
open_to_ideas = '//*[@id="retrospective_partner_learn_style_feedback_open_to_my_ideas"]'
professional = '//*[@id="retrospective_partner_learn_style_feedback_professional"]'
motivated = '//*[@id="retrospective_partner_learn_style_feedback_motivated"]'
inspiring = '//*[@id="retrospective_partner_learn_style_feedback_inspiring"]'
patient = '//*[@id="retrospective_partner_learn_style_feedback_patient"]'
supportive = '//*[@id="retrospective_partner_learn_style_feedback_supportive"]'
friendly = '//*[@id="retrospective_partner_learn_style_feedback_friendly"]'
most_times = '//*[@id="retrospective_switch_roles_most_of_the_time"]'
standup_enjoy = '//*[@id="retrospective_standup_enjoyment"]'
standup_daily_structure = '//*[@id="retrospective_standup_team_alignment_feedback"]'
networking = '//*[@id="retrospective_networking_activity"]'
microverse_recommend = '//*[@id="retrospective_recommend_microverse"]'
friday_submit = '//*[@id="new_retrospective"]/div[2]/input'
partner_rating_array = [faster, experienced, punctual, good_com,
                        great_collab, open_to_ideas, professional, motivated, inspiring, patient,
                        supportive, friendly, most_times]

# Esperar a que cargue la pagina antes de poner los datos
sleep(5)

# Login block
driver.find_element_by_xpath(mail_input).send_keys(email)
driver.find_element_by_xpath(password_input).send_keys(password)
driver.find_element_by_xpath(login_button).click()
sleep(3)

# Navegar a las formas
# driver.find_element_by_xpath(week_back_button).click()
sleep(2)

# Abrir dia de la semana correspondiente
if current_day == "Monday":
    driver.find_element_by_css_selector()(monday_standup).click()
elif current_day == "Tuesday":
    driver.find_element_by_css_selector(tuesday_standup).click()
elif current_day == "Wednesday":
    driver.find_element_by_css_selector()(wednesday_standup).click()
elif current_day == "Thursday":
    driver.find_element_by_css_selector()(thursday_standup).click()
elif current_day == "Friday":
    driver.find_element_by_css_selector()(friday_standup).click()
else:
    print(f"""{notice}
  Can't do weekends yet :P
{notice}""")
    driver.quit()
    exit()

sleep(2)

# Cambiar a la ventana actual
driver.switch_to.window(driver.window_handles[-1])

# Llenar forma
if current_day in same_form_days:
    three_goals = Select(driver.find_element_by_xpath(achieved_goals))
    sleep(1)
    three_goals.select_by_value("Some of them")
    sleep(1)
    driver.find_element_by_xpath(went_well).send_keys(
        "Continued with the technical curriculum")
    driver.execute_script("window.scrollTo(0, 600)")
    sleep(1)
    driver.find_element_by_xpath(nothing_wrong).click()
    sleep(1)
    driver.find_element_by_xpath(goal1).send_keys(
        "To continue with the technical curriculum")
    driver.find_element_by_xpath(goal2).send_keys(
        "To continue with the professional curriculum")
    driver.find_element_by_xpath(goal3).send_keys(
        "To continue with the coding challenges")
    driver.find_element_by_xpath(rest).send_keys("To take some rest")
    driver.execute_script("window.scrollTo(0, 1080)")
    driver.find_element_by_xpath(happy_face).click()
else:
    three_goals = Select(driver.find_element_by_xpath(friday_achieved_goals))
    sleep(1)
    three_goals.select_by_value("Some of them")
    sleep(1)
    driver.find_element_by_xpath(friday_nothing_wrong).click()
    sleep(1)
    driver.find_element_by_xpath(friday_went_well).send_keys(
        "Continued with the technical curriculum")
    driver.execute_script("window.scrollTo(0, 600)")
    sleep(1)
    driver.find_element_by_xpath(friday_goal1).send_keys(
        "To continue with the professional curriculum")
    driver.find_element_by_xpath(friday_goal2).send_keys(
        "To continue with the technical curriculum")
    driver.find_element_by_xpath(friday_goal3).send_keys(
        "To continue with the coding challenges")
    sleep(2)
    driver.find_element_by_xpath(friday_rest).send_keys("To take some rest")
    sleep(1)
    # Partner rating
    for x in partner_rating_array:
      multiple_selection(x)

    # Standup team rating
    standup_rating = Select(driver.find_element_by_xpath(standup_enjoy))
    sleep(1)
    standup_rating.select_by_value("10")
    sleep(1)
    standup_rating = Select(driver.find_element_by_xpath(standup_daily_structure))
    sleep(1)
    standup_rating.select_by_value("Often")
    sleep(1)
    standup_rating = Select(driver.find_element_by_xpath(networking))
    sleep(1)
    standup_rating.select_by_value("Other")
    sleep(1)
    standup_rating = Select(driver.find_element_by_xpath(microverse_recommend))
    sleep(1)
    standup_rating.select_by_value("10")
    sleep(1)

# Mandar forma
# driver.find_element_by_xpath(submit).click()

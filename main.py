import time

import constants
import selenium_util


def main():
    driver = None
    try:
        driver = selenium_util.connect_to_portal()
        selenium_util.login_to_portal(driver)
        time.sleep(20)

        selenium_util.click_registration(driver)
        time.sleep(5)

        for semester_num, course_num_list in enumerate(constants.COURSES):
            selenium_util.click_semester_reg(driver, semester_num)
            time.sleep(5)

            for course_num in course_num_list:
                selenium_util.click_course_reg(driver, course_num)

                time.sleep(5)

                selenium_util.try_reg_to_course(driver)

                time.sleep(5)

                selenium_util.uncheck_first_checkbox(driver)

                time.sleep(5)
            break

        time.sleep(15)
    finally:
        selenium_util.close_portal(driver)


if __name__ == '__main__':
    main()


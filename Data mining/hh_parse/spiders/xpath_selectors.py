PAGINATION = {
    "selector": "//a[@data-qa='pager-page']"
                "/@href",
    "callback": "parse_jobs"
}

JOBS = {
    "selector": "//a[@data-qa='vacancy-serp__vacancy-title']"
                "/@href",
    "callback": "parse_job"
}

JOB_DATA = {
    "title": "//h1[@data-qa='vacancy-title']"
             "/text()",
    "salary": "//p[@class='vacancy-salary']"
              "//text()",
    "description": "//div[@data-qa='vacancy-description']"
                   "//text()",
    "key_skills": "//div[@class='bloko-tag-list']"
                  "//span[@data-qa='bloko-tag__text']"
                  "/text()",
    "author_href": "//a[@data-qa='vacancy-company-name']"
                   "/@href"
}

AUTHOR = {
    "selector": "//a[@data-qa='vacancy-serp__vacancy-title']"
                "/@href",
    "callback": "parse_job"
}

AUTHOR_DATA = {
    "name": "//span[@data-qa='company-header-title-name']"
            "/text()",
    "author_url": "//a[@data-qa='sidebar-company-site']"
                  "/@href",
    "areas": "//div[@class='employer-sidebar-block']"
             "//p"
             "/text()",
    "author_description": "//div[@data-qa='company-description-text']"
                          "//text()"
}
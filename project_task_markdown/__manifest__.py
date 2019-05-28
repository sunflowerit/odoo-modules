# -*- coding: utf-8 -*-
# Copyright 2016-2019 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Markdown on project tasks',
    'version': '10.0.1.0.0',
    'category': 'Project Management',
    'summary': 'Adds markdown markup to all project task descriptions.',
    'author': 'Sunflower IT',
    'website': 'http://sunflowerweb.nl',
    'depends': [
        'web_widget_text_markdown',
        'project_task_html_description',
        'project'
    ],
    'data': [
        'views/project_task.xml'
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError

from openerp.tools import mute_logger

from openerp.tests.common import TransactionCase

class GlobalTestOpenAcademyCourse(TransactionCase):
    '''
    Global test to openacademy course model.
    Test create course and trigger constraints.
    '''

    # Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to test methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.variable = 'hello world'
        self.course = self.env['openacademy.course']

    # Method of class that don't is test
    def create_course(self, course_name, course_description, 
            course_responsible_id):
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id, 
            })
        return course_id

    # Method of test startswith 'def test_*(self):'
    @mute_logger('openerp.sql_db')   # Mute openerp.sql_db error to avoid it in log
    def test_10_same_name_description(self):
        '''
        Test create a course with equals name and description.
        To raise constraint of name different to description.
        '''
        # Error raised expected with message expected
        with self.assertRaisesRegexp(
                IntegrityError, 
                'new row for relation "openacademy_course" violates'
                ' check constraint "openacademy_course_name_description_check"'
                ):
            # Create a course with name and description equals, to raise error
            self.create_course('test','test',None)

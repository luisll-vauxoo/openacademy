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

    @mute_logger('openerp.sql_db')   # Mute openerp.sql_db error to avoid it in log
    def test_20_two_course_same_name(self):
        '''
        Test to create two courses with same name.
        To test constraint of unique name.
        '''
        new_id = self.create_course('test1','test_description',None)
        print "new_id", new_id
        with self.assertRaisesRegexp(
                IntegrityError, 
                'duplicate key value violates unique'
                ' constraint "openacademy_course_name_unique"'
                ):
            new_id2 = self.create_course('test1','test_description',None)
            print "new_id2", new_id2

    def test_15_duplicate_course(self):
        '''
        Test to duplicate a course and check that work fine!
        '''
        course = self.env.ref('openacademy.course0')
        #import pdb; pdb.set_trace()
        course_id = course.copy()
        print "course_id", course_id


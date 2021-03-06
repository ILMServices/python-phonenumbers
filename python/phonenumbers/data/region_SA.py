"""Auto-generated file, do not edit by hand. SA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SA = PhoneMetadata(id='SA', country_code=966, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{7,8}|(?:[2-467]|92)\\d{7}|5\\d{8}|8\\d{9}', possible_number_pattern='\\d{7,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='11\\d{7}|1?(?:2[24-8]|3[35-8]|4[3-68]|6[2-5]|7[235-7])\\d{6}', possible_number_pattern='\\d{7,9}', example_number='112345678'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5[013-689]|811)\\d{7}', possible_number_pattern='\\d{9,10}', example_number='512345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', possible_number_pattern='\\d{10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='92[05]\\d{6}', possible_number_pattern='\\d{9}', example_number='920012345'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([1-467])(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[1-467]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1[1-467]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(5\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['5'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(92\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['92'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(800)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['80'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(811)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['81'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)

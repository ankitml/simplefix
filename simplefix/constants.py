#! /usr/bin/env python
########################################################################
# SimpleFIX
# Copyright (C) 2017, David Arnold.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
########################################################################

"""FIX protocol constants."""

import sys


if sys.version_info.major == 2:
    EQUALS_BYTE = b'='
    SOH_BYTE = b'\x01'
    SOH_STR = SOH_BYTE
else:
    EQUALS_BYTE = 61
    SOH_BYTE = 1
    SOH_STR = b'\x01'

# Tag 1
TAG_ACCOUNT = b'1'

# Tag 2
TAG_ADVID = b'2'

# Tag 3
TAG_ADVREFID = b'3'

# Tag 4
TAG_ADVSIDE = b'4'
ADVSIDE_BUY = b'B'
ADVSIDE_CROSS = b'X'
ADVSIDE_SELL = b'S'
ADVSIDE_TRADE = b'T'

# Tag 5
TAG_ADVTRANSTYPE = b'5'
ADVTRANSTYPE_CANCEL = b'C'
ADVTRANSTYPE_NEW = b'N'
ADVTRANSTYPE_REPLACE = b'R'

# Tag 6
TAG_AVGPX = b'6'

# Tag 7
TAG_BEGINSEQNO = b'7'

# Tag 8
TAG_BEGINSTRING = b'8'

# Tag 9
TAG_BODYLENGTH = b'9'

# Tag 10
TAG_CHECKSUM = b'10'

# Tag 11
TAG_CLORDID = b'11'

# Tag 12
TAG_COMMISSION = b'12'

# Tag 13
TAG_COMMTYPE = b'13'
COMMTYPE_PER_UNIT = b'1'
COMMTYPE_PERCENT = b'2'
COMMTYPE_ABSOLUTE = b'3'
COMMTYPE_PERCENT_WAIVED_CASH = b'4'
COMMTYPE_PERCENT_WAIVED_ENHANCED = b'5'
COMMTYPE_POINTS = b'6'

# Tag 14
TAG_CUMQTY = b'14'

# Tag 15
TAG_CURRENCY = b'15'
CURRENCY_AFGHANI = b'AFA'
CURRENCY_ALGERIAN_DINAR = b'DZD'
CURRENCY_ANDORRAN_PESETA = b'ADP'
CURRENCY_ARGENTINE_PESO = b'ARS'
CURRENCY_ARMENIAN_DRAM = b'AMD'
CURRENCY_ARUBAN_GUILDER = b'AWG'
CURRENCY_AUSTRALIAN_DOLLAR = b'AUD'
CURRENCY_AZERBAIJANIAN_MANAT = b'AZM'
CURRENCY_BAHAMIAN_DOLLAR = b'BSD'
# FIXME: many, many, more.

# Tag 16
TAG_ENDSEQNO = b'16'

# Tag 17
TAG_EXECID = b'17'

# Tag 18
TAG_EXECINST = b'18'
EXECINST_NOT_HELD = b'1'
EXECINST_WORK = b'2'
EXECINST_GO_ALONG = b'3'
EXECINST_OVER_THE_DAY = b'4'
EXECINST_HELD = b'5'
EXECINST_PARTICIPATE_DONT_INITIATE = b'6'
EXECINST_STRICT_SCALE = b'7'
EXECINST_TRY_TO_SCALE = b'8'
EXECINST_STAY_ON_BID_SIDE = b'9'
EXECINST_STAY_ON_OFFER_SIDE = b'0'
EXECINST_NO_CROSS = b'A'
EXECINST_OK_TO_CROSS = b'B'
EXECINST_CALL_FIRST = b'C'
EXECINST_PERCENT_OF_VOLUME = b'D'
EXECINST_DO_NOT_INCREASE = b'E'
EXECINST_DO_NOT_REDUCE = b'F'
EXECINST_ALL_OR_NONE = b'G'
EXECINST_REINSTATE_ON_SYSTEM_FAILURE = b'H'
EXECINST_INSTITUTIONS_ONLY = b'I'
EXECINST_REINSTATE_ON_TRADING_HALT = b'J'
EXECINST_CANCEL_ON_TRADING_HALT = b'K'
EXECINST_LAST_PEG = b'L'
EXECINST_MID_PRICE_PEG = b'M'
EXECINST_NON_NEGOTIABLE = b'N'
EXECINST_OPENING_PEG = b'O'
EXECINST_MARKET_PEG = b'P'
EXECINST_CANCEL_ON_SYSTEM_FAILURE = b'Q'
EXECINST_PRIMARY_PEG = b'R'
EXECINST_SUSPEND = b'S'
EXECINST_CUSTOMER_DISPLAY_INSTRUCTION = b'U'
EXECINST_NETTING = b'V'
EXECINST_PEG_TO_VWAP = b'W'
EXECINST_TRADE_ALONG = b'X'
EXECINST_TRY_TO_STOP = b'Y'
EXECINST_CANCEL_IF_NOT_BEST = b'Z'
EXECINST_TRAILING_STOP_PEG = b'a'
EXECINST_STRICT_LIMIT = b'b'
EXECINST_IGNORE_PRICE_VALIDITY_CHECKS = b'c'
EXECINST_PEG_TO_LIMIT_PRICE = b'd'
EXECINST_WORK_TO_TARGET_STRATEGY = b'e'



# Tag 35
TAG_MSGTYPE = b'35'
MSGTYPE_HEARTBEAT = b'0'
MSGTYPE_TEST_REQUEST = b'1'
MSGTYPE_RESEND_REQUEST = b'2'
MSGTYPE_REJECT = b'3'
MSGTYPE_SEQUENCE_RESET = b'4'
MSGTYPE_LOGOUT = b'5'
MSGTYPE_INDICATION_OF_INTEREST = b'6'
MSGTYPE_ADVERTISEMENT = b'7'
MSGTYPE_EXECUTION_REPORT = b'8'
MSGTYPE_ORDER_CANCEL_REJECT = b'9'
MSGTYPE_LOGON = b'A'
MSGTYPE_NEWS = b'B'
MSGTYPE_EMAIL = b'C'
MSGTYPE_NEW_ORDER_SINGLE = b'D'
MSGTYPE_NEW_ORDER_LIST = b'E'
MSGTYPE_ORDER_CANCEL_REQUEST = b'F'
MSGTYPE_ORDER_CANCEL_REPLACE_REQUEST = b'G'
MSGTYPE_ORDER_STATUS_REQUEST = b'H'
MSGTYPE_ALLOCATION = b'J'
MSGTYPE_LIST_CANCEL_REQUEST = b'K'
MSGTYPE_LIST_EXECUTE = b'L'
MSGTYPE_LIST_STATUS_REQUEST = b'M'
MSGTYPE_LIST_STATUS = b'N'
MSGTYPE_ALLOCATION_ACK = b'P'
MSGTYPE_DONT_KNOW_TRADE = b'Q'
MSGTYPE_QUOTE_REQUEST = b'R'
MSGTYPE_QUOTE = b'S'
MSGTYPE_SETTLEMENT_INSTRUCTIONS = b'T'
MSGTYPE_MARKET_DATA_REQUEST = b'V'
MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH = b'W'
MSGTYPE_MARKET_DATA_INCREMENTAL_REFRESH = b'X'
MSGTYPE_MARKET_DATA_REQUEST_REJECT = b'Y'
MSGTYPE_QUOTE_CANCEL = b'Z'
MSGTYPE_QUOTE_STATUS_REQUEST = b'a'
MSGTYPE_QUOTE_ACKNOWLEDGEMENT = b'b'
MSGTYPE_SECURITY_DEFINITION_REQUEST = b'c'
MSGTYPE_SECURITY_DEFINITION = b'd'
MSGTYPE_SECURITY_STATUS_REQUEST = b'e'
MSGTYPE_SECURITY_STATUS = b'f'
MSGTYPE_TRADING_SESSION_STATUS_REQUEST = b'g'
MSGTYPE_TRADING_SESSION_STATUS = b'h'
MSGTYPE_MASS_QUOTE = b'i'
MSGTYPE_BUSINESS_MESSAGE_REJECT = b'j'
MSGTYPE_BID_REQUEST = b'k'
MSGTYPE_BID_RESPONSE = b'l'
MSGTYPE_LIST_STRIKE_PRICE = b'm'
MSGTYPE_XML_MESSAGE = b'n'
MSGTYPE_REGISTRATION_INSTRUCTIONS = b'o'
MSGTYPE_REGISTRATION_INSTRUCTIONS_RESPONSE = b'p'
MSGTYPE_ORDER_MASS_CANCEL_REQUEST = b'q'
MSGTYPE_ORDER_MASS_CANCEL_REPORT = b'r'
MSGTYPE_NEW_ORDER_CROSS = b's'
MSGTYPE_CROSS_ORDER_CANCEL_REPLACE_REQUEST = b't'
MSGTYPE_CROSS_ORDER_CANCEL_REQUEST = b'u'
MSGTYPE_SECURITY_TYPE_REQUEST = b'v'
MSGTYPE_SECURITY_TYPES = b'w'
MSGTYPE_SECURITY_LIST_REQUEST = b'x'
MSGTYPE_SECURITY_LIST = b'y'
MSGTYPE_DERIVATIVE_SECURITY_LIST_REQUEST = b'z'
MSGTYPE_DERIVATIVE_SECURITY_LIST = b'AA'
MSGTYPE_NEW_ORDER_MULTILEG = b'AB'
MSGTYPE_MULTILEG_ORDER_CANCEL_REPLACE_REQUEST = b'AC'
MSGTYPE_TRADE_CAPTURE_REPORT_REQUEST = b'AD'
MSGTYPE_TRADE_CAPTURE_REPORT = b'AE'
MSGTYPE_ORDER_MASS_STATUS_REQUEST = b'AF'
MSGTYPE_QUOTE_REQUEST_REJECT = b'AG'
MSGTYPE_RFQ_REQUEST = b'AH'
MSGTYPE_QUOTE_STATUS_REPORT = b'AI'
MSGTYPE_QUOTE_RESPONSE = b'AJ'
MSGTYPE_CONFIRMATION = b'AK'
MSGTYPE_POSITION_MAINTENANCE_REQUEST = b'AL'
MSGTYPE_POSITION_MAINTENANCE_REPORT = b'AM'
MSGTYPE_REQUEST_FOR_POSITIONS = b'AN'
MSGTYPE_REQUEST_FOR_POSITIONS_ACK = b'AO'
MSGTYPE_POSITION_REPORT = b'AP'
MSGTYPE_TRADE_CAPTURE_REPORT_REQUEST_ACK = b'AQ'
MSGTYPE_TRADE_CAPTURE_REPORT_ACK = b'AR'
MSGTYPE_ALLOCATION_REPORT = b'AS'
MSGTYPE_ALLOCATION_REPORT_ACK = b'AT'
MSGTYPE_CONFIRMATION_ACK = b'AU'
MSGTYPE_SETTLEMENT_INSTRUCTION_REQUEST = b'AV'
MSGTYPE_ASSIGNMENT_REPORT = b'AW'
MSGTYPE_COLLATERAL_REQUEST = b'AX'
MSGTYPE_COLLATERAL_ASSIGNMENT = b'AY'
MSGTYPE_COLLATERAL_RESPONSE = b'AZ'
MSGTYPE_COLLATERAL_REPORT = b'BA'
MSGTYPE_COLLATERAL_INQUIRY = b'BB'
MSGTYPE_NETWORK_STATUS_REQUEST = b'BC'
MSGTYPE_NETWORK_STATUS_RESPONSE = b'BD'
MSGTYPE_USER_REQUEST = b'BE'
MSGTYPE_USER_RESPONSE = b'BF'
MSGTYPE_COLLATERAL_INQUIRY_ACK = b'BG'
MSGTYPE_CONFIRMATION_REQUEST = b'BH'

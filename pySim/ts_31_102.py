#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Various constants from ETSI TS 131 102
"""

#
# Copyright (C) 2020 Supreeth Herle <herlesupreeth@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# Mapping between USIM Service Number and its description
EF_UST_map = {
	1: 'Local Phone Book',
	2: 'Fixed Dialling Numbers (FDN)',
	3: 'Extension 2',
	4: 'Service Dialling Numbers (SDN)',
	5: 'Extension3',
	6: 'Barred Dialling Numbers (BDN)',
	7: 'Extension4',
	8: 'Outgoing Call Information (OCI and OCT)',
	9: 'Incoming Call Information (ICI and ICT)',
	10: 'Short Message Storage (SMS)',
	11: 'Short Message Status Reports (SMSR)',
	12: 'Short Message Service Parameters (SMSP)',
	13: 'Advice of Charge (AoC)',
	14: 'Capability Configuration Parameters 2 (CCP2)',
	15: 'Cell Broadcast Message Identifier',
	16: 'Cell Broadcast Message Identifier Ranges',
	17: 'Group Identifier Level 1',
	18: 'Group Identifier Level 2',
	19: 'Service Provider Name',
	20: 'User controlled PLMN selector with Access Technology',
	21: 'MSISDN',
	22: 'Image (IMG)',
	23: 'Support of Localised Service Areas (SoLSA)',
	24: 'Enhanced Multi-Level Precedence and Pre-emption Service',
	25: 'Automatic Answer for eMLPP',
	26: 'RFU',
	27: 'GSM Access',
	28: 'Data download via SMS-PP',
	29: 'Data download via SMS-CB',
	30: 'Call Control by USIM',
	31: 'MO-SMS Control by USIM',
	32: 'RUN AT COMMAND command',
	33: 'shall be set to 1',
	34: 'Enabled Services Table',
	35: 'APN Control List (ACL)',
	36: 'Depersonalisation Control Keys',
	37: 'Co-operative Network List',
	38: 'GSM security context',
	39: 'CPBCCH Information',
	40: 'Investigation Scan',
	41: 'MexE',
	42: 'Operator controlled PLMN selector with Access Technology',
	43: 'HPLMN selector with Access Technology',
	44: 'Extension 5',
	45: 'PLMN Network Name',
	46: 'Operator PLMN List',
	47: 'Mailbox Dialling Numbers',
	48: 'Message Waiting Indication Status',
	49: 'Call Forwarding Indication Status',
	50: 'Reserved and shall be ignored',
	51: 'Service Provider Display Information',
	52: 'Multimedia Messaging Service (MMS)',
	53: 'Extension 8',
	54: 'Call control on GPRS by USIM',
	55: 'MMS User Connectivity Parameters',
	56: 'Network\'s indication of alerting in the MS (NIA)',
	57: 'VGCS Group Identifier List (EFVGCS and EFVGCSS)',
	58: 'VBS Group Identifier List (EFVBS and EFVBSS)',
	59: 'Pseudonym',
	60: 'User Controlled PLMN selector for I-WLAN access',
	61: 'Operator Controlled PLMN selector for I-WLAN access',
	62: 'User controlled WSID list',
	63: 'Operator controlled WSID list',
	64: 'VGCS security',
	65: 'VBS security',
	66: 'WLAN Reauthentication Identity',
	67: 'Multimedia Messages Storage',
	68: 'Generic Bootstrapping Architecture (GBA)',
	69: 'MBMS security',
	70: 'Data download via USSD and USSD application mode',
	71: 'Equivalent HPLMN',
	72: 'Additional TERMINAL PROFILE after UICC activation',
	73: 'Equivalent HPLMN Presentation Indication',
	74: 'Last RPLMN Selection Indication',
	75: 'OMA BCAST Smart Card Profile',
	76: 'GBA-based Local Key Establishment Mechanism',
	77: 'Terminal Applications',
	78: 'Service Provider Name Icon',
	79: 'PLMN Network Name Icon',
	80: 'Connectivity Parameters for USIM IP connections',
	81: 'Home I-WLAN Specific Identifier List',
	82: 'I-WLAN Equivalent HPLMN Presentation Indication',
	83: 'I-WLAN HPLMN Priority Indication',
	84: 'I-WLAN Last Registered PLMN',
	85: 'EPS Mobility Management Information',
	86: 'Allowed CSG Lists and corresponding indications',
	87: 'Call control on EPS PDN connection by USIM',
	88: 'HPLMN Direct Access',
	89: 'eCall Data',
	90: 'Operator CSG Lists and corresponding indications',
	91: 'Support for SM-over-IP',
	92: 'Support of CSG Display Control',
	93: 'Communication Control for IMS by USIM',
	94: 'Extended Terminal Applications',
	95: 'Support of UICC access to IMS',
	96: 'Non-Access Stratum configuration by USIM',
	97: 'PWS configuration by USIM',
	98: 'RFU',
	99: 'URI support by UICC',
	100: 'Extended EARFCN support',
	101: 'ProSe',
	102: 'USAT Application Pairing',
	103: 'Media Type support',
	104: 'IMS call disconnection cause',
	105: 'URI support for MO SHORT MESSAGE CONTROL',
	106: 'ePDG configuration Information support',
	107: 'ePDG configuration Information configured',
	108: 'ACDC support',
	109: 'MCPTT',
	110: 'ePDG configuration Information for Emergency Service support',
	111: 'ePDG configuration Information for Emergency Service configured',
}

EF_USIM_ADF_map = {
	'LI': '6F05',
	'ARR': '6F06',
	'IMSI': '6F07',
	'Keys': '6F08',
	'KeysPS': '6F09',
	'DCK': '6F2C',
	'HPPLMN': '6F31',
	'CNL': '6F32',
	'ACMmax': '6F37',
	'UST': '6F38',
	'ACM': '6F39',
	'FDN': '6F3B',
	'SMS': '6F3C',
	'GID1': '6F3E',
	'GID2': '6F3F',
	'MSISDN': '6F40',
	'PUCT': '6F41',
	'SMSP': '6F42',
	'SMSS': '6F42',
	'CBMI': '6F45',
	'SPN': '6F46',
	'SMSR': '6F47',
	'CBMID': '6F48',
	'SDN': '6F49',
	'EXT2': '6F4B',
	'EXT3': '6F4C',
	'BDN': '6F4D',
	'EXT5': '6F4E',
	'CCP2': '6F4F',
	'CBMIR': '6F50',
	'EXT4': '6F55',
	'EST': '6F56',
	'ACL': '6F57',
	'CMI': '6F58',
	'START-HFN': '6F5B',
	'THRESHOLD': '6F5C',
	'PLMNwAcT': '6F60',
	'OPLMNwAcT': '6F61',
	'HPLMNwAcT': '6F62',
	'PSLOCI': '6F73',
	'ACC': '6F78',
	'FPLMN': '6F7B',
	'LOCI': '6F7E',
	'ICI': '6F80',
	'OCI': '6F81',
	'ICT': '6F82',
	'OCT': '6F83',
	'AD': '6FAD',
	'VGCS': '6FB1',
	'VGCSS': '6FB2',
	'VBS': '6FB3',
	'VBSS': '6FB4',
	'eMLPP': '6FB5',
	'AAeM': '6FB6',
	'ECC': '6FB7',
	'Hiddenkey': '6FC3',
	'NETPAR': '6FC4',
	'PNN': '6FC5',
	'OPL': '6FC6',
	'MBDN': '6FC7',
	'EXT6': '6FC8',
	'MBI': '6FC9',
	'MWIS': '6FCA',
	'CFIS': '6FCB',
	'EXT7': '6FCC',
	'SPDI': '6FCD',
	'MMSN': '6FCE',
	'EXT8': '6FCF',
	'MMSICP': '6FD0',
	'MMSUP': '6FD1',
	'MMSUCP': '6FD2',
	'NIA': '6FD3',
	'VGCSCA': '6FD4',
	'VBSCA': '6FD5',
	'GBAP': '6FD6',
	'MSK': '6FD7',
	'MUK': '6FD8',
	'EHPLMN': '6FD9',
	'GBANL': '6FDA',
	'EHPLMNPI': '6FDB',
	'LRPLMNSI': '6FDC',
	'NAFKCA': '6FDD',
	'SPNI': '6FDE',
	'PNNI': '6FDF',
	'NCP-IP': '6FE2',
	'EPSLOCI': '6FE3',
	'EPSNSC': '6FE4',
	'UFC': '6FE6',
	'UICCIARI': '6FE7',
	'NASCONFIG': '6FE8',
	'PWC': '6FEC',
	'FDNURI': '6FED',
	'BDNURI': '6FEE',
	'SDNURI': '6FEF',
	'IWL': '6FF0',
	'IPS': '6FF1',
	'IPD': '6FF2',
	'ePDGId': '6FF3',
	'ePDGSelection': '6FF4',
	'ePDGIdEm': '6FF5',
	'ePDGSelectionEm': '6FF6',
}

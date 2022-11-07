import os

TAPE_PRETRAIN_PATH='tape-neurips2019/pretrained_models/'
TAPE_MODEL_LOCATIONS = {"resnet": os.path.join(TAPE_PRETRAIN_PATH, "resnet_weights.h5"),
                        "bepler": os.path.join(TAPE_PRETRAIN_PATH, "bepler_unsupervised_pretrain_weights.h5"),
                        "unirep": os.path.join(TAPE_PRETRAIN_PATH, "unirep_weights.h5"),
                        "transformer": os.path.join(TAPE_PRETRAIN_PATH, "transformer_weights.h5"),
                        "lstm": os.path.join(TAPE_PRETRAIN_PATH, "lstm_weights.h5")}

UNIREP_PATH='unirep_weights/'
ESM_MODEL_PATH='esm_weights/'
ESM_MODEL_LOCATIONS={'esm1b':ESM_MODEL_PATH+'esm1b_t33_650M_UR50S.pt',
                     'esm1v':ESM_MODEL_PATH+'esm1v_t33_650M_UR90S_1.pt',}

Chain_dir={'KKA2_KLEPN':'A',
           'BLAT_ECOLX':'A',
           'BRCA1_HUMAN':'A',
           'DLG4_RAT':'A',
           'GAL4_YEAST':'A',
           'HSP82_YEAST':'A',
           'YAP1_HUMAN':'A',
           'RL401_YEAST':'E',
           'PABP_YEAST':'D',
           'GFP_AEQVI':'A',
           'MTH3_HAEAE':'A',
           'UBE4B_MOUSE':'A',
           'AMIE_PSEAE':'A',
           'CALM1_HUMAN':'A',
           'TPK1_HUMAN':'A',
           'UBC9_HUMAN':'A',
           'SUMO1_HUMAN':'B',
           'RASH_HUMAN':'A',
           'TRPC_SULSO':'A',
           'B3VI55_LIPST':'A',
           'B3VI55_LIPSTSTABLE':'A',
           'TRPC_THEMA':'A',
           'TPMT_HUMAN':'A',
           'P84126_THETH':'A',
           'MK01_HUMAN':'A',
           'PTEN_HUMAN':'A',
           'IF1_ECOLI':'A',
           'GB1':'A',
           }
Uniprot_to_PDB={'KKA2_KLEPN':{'default':'1nd4'},
                'BLAT_ECOLX':{'default':'1m40'},
                'BRCA1_HUMAN':{'default':'1jm7','AF':'AF-P38398','NMR':'1jm7'},
                'DLG4_RAT':{'default':'1tp5'},
                'GAL4_YEAST':{'default':'AF-P04386'},
                'HSP82_YEAST':{'default':'AF-P02829'},
                'YAP1_HUMAN':{'default':'4rex'},
                'RL401_YEAST':{'default':'6nyo'},
                'PABP_YEAST':{'default':'6r5k'},
                'GFP_AEQVI':{'default':'2wur'},
                'MTH3_HAEAE':{'default':'1dct'},
                'UBE4B_MOUSE':{'default':'2kr4','NMR':'2kr4'},
                'AMIE_PSEAE':{'default':'2uxy'},
                'CALM1_HUMAN':{'default':'1cll'},
                'TPK1_HUMAN':{'default':'3s4y'},
                'UBC9_HUMAN':{'default':'1a3s'},
                'SUMO1_HUMAN':{'default':'2uyz'},
                'RASH_HUMAN':{'default':'121p'},
                'TRPC_SULSO':{'default':'1igs'},
                'B3VI55_LIPST':{'default':'4zfv'},
                'B3VI55_LIPSTSTABLE':{'default':'4zfv'},
                'TRPC_THEMA':{'default':'1i4n'},
                'TPMT_HUMAN':{'default':'2bzg'},
                'P84126_THETH':{'default':'1vc4'},
                'MK01_HUMAN':{'default':'2ojg'},
                'PTEN_HUMAN':{'default':'AF-P60484-F1-model_v2'},
                'IF1_ECOLI':{'default':'1ah9','NMR':'1ah9','AF':'AF-P69222-F1-model_v2'},
                'GB1':{'default':'1pga'}
                }
dataset_to_uniprot={'KKA2_KLEPN_Mikkelsen2014-Kan18_avg':'KKA2_KLEPN',
                    'BLAT_ECOLX_Palzkill2012-ddG_stat':'BLAT_ECOLX',
                    'BLAT_ECOLX_Tenaillon2013-singles-MIC_score':'BLAT_ECOLX',
                    'BLAT_ECOLX_Ranganathan2015-2500':'BLAT_ECOLX',
                    'BLAT_ECOLX_Ostermeier2014-linear':'BLAT_ECOLX',
                    'BRCA1_HUMAN_Fields2015-e3':'BRCA1_HUMAN',
                    'BRCA1_HUMAN_Fields2015-y2h':'BRCA1_HUMAN',
                    'DLG4_RAT_Ranganathan2012-CRIPT':'DLG4_RAT',
                    'GAL4_YEAST_Shendure2015-SEL_C_40h':'GAL4_YEAST',
                    'HSP82_YEAST_Bolon2016-selection_coefficient':'HSP82_YEAST',
                    'YAP1_HUMAN_Fields2012-singles-linear':'YAP1_HUMAN',
                    'RL401_YEAST_Bolon2013-selection_coefficient':'RL401_YEAST',
                    'RL401_YEAST_Bolon2014-react_rel':'RL401_YEAST',
                    'PABP_YEAST_Fields2013-linear':'PABP_YEAST',
                    'GFP_AEQVI_Sarkisyan2016':'GFP_AEQVI',
                    'MTH3_HAEAESTABILIZED_Tawfik2015-Wrel_G17_filtered':'MTH3_HAEAE',
                    'UBE4B_MOUSE_Klevit2013-nscor_log2_ratio':'UBE4B_MOUSE',
                    'UBE4B_MOUSE_Klevit2013-nscor_log2_ratio_single':'UBE4B_MOUSE',
                    'RL401_YEAST_Mavor2016_DMSO':'RL401_YEAST',
                    'AMIE_PSEAE_Wrenbeck2017_isobutyramide_normalized_fitness':'AMIE_PSEAE',
                    'CALM1_HUMAN_Roth2017_screenscore':'CALM1_HUMAN',
                    'TPK1_HUMAN_Roth2017_screenscore':'TPK1_HUMAN',
                    'UBC9_HUMAN_Roth2017_screenscore':'UBC9_HUMAN',
                    'SUMO1_HUMAN_Roth2017_screenscore':'SUMO1_HUMAN',
                    'RASH_HUMAN_Bandaru2016_unregulated':'RASH_HUMAN',
                    'TRPC_SULSO_Chen2017_fitness':'TRPC_SULSO',
                    'B3VI55_LIPST_Klesmith2015_SelectionOne':'B3VI55_LIPST',
                    'B3VI55_LIPSTSTABLE_Klesmith2015_SelectionTwo':'B3VI55_LIPSTSTABLE',
                    'TRPC_THEMA_Chen2017_fitness':'TRPC_THEMA',
                    'TPMT_HUMAN_Matreyek2019_score':'TPMT_HUMAN',
                    'P84126_THETH_Chen2017_fitness':'P84126_THETH',
                    'MK01_HUMAN_Brenan2016_DOX_Average':'MK01_HUMAN',
                    'PTEN_HUMAN_Matreyek2019_score':'PTEN_HUMAN',
                    'IF1_ECOLI_Kelsic2016_fitness_rich':'IF1_ECOLI',
                    'GB1_Olson2014_ddg':'GB1',
                    'GB1_Wu2016_ddg':'GB1'}

dataset_to_n_structure={'BRCA1_HUMAN_Fields2015-e3_NMR':14,
                        'BRCA1_HUMAN_Fields2015-y2h_NMR':14,
                        'IF1_ECOLI_Kelsic2016_fitness_rich_NMR':19,
                        'UBE4B_MOUSE_Klevit2013-nscor_log2_ratio_single_NMR':20,

}


STUCTURE_TYPE={
          'GFP_AEQVI_Sarkisyan2016':'X-ray',
          'GB1_Olson2014_ddg':'X-ray',
          'KKA2_KLEPN_Mikkelsen2014-Kan18_avg':'X-ray',
          'BLAT_ECOLX_Ostermeier2014-linear':'X-ray',
          'BLAT_ECOLX_Tenaillon2013-singles-MIC_score':'X-ray',
          'BLAT_ECOLX_Palzkill2012-ddG_stat':'X-ray',
          'BLAT_ECOLX_Ranganathan2015-2500':'X-ray',
          'DLG4_RAT_Ranganathan2012-CRIPT':'X-ray',
          'YAP1_HUMAN_Fields2012-singles-linear':'X-ray',
          'RL401_YEAST_Bolon2013-selection_coefficient':'X-ray',
          'RL401_YEAST_Bolon2014-react_rel':'X-ray',
          'RL401_YEAST_Mavor2016_DMSO':'X-ray',
          'MTH3_HAEAESTABILIZED_Tawfik2015-Wrel_G17_filtered':'X-ray',
          'AMIE_PSEAE_Wrenbeck2017_isobutyramide_normalized_fitness':'X-ray',
          'CALM1_HUMAN_Roth2017_screenscore':'X-ray',
          'TRPC_SULSO_Chen2017_fitness':'X-ray',
          'TPK1_HUMAN_Roth2017_screenscore':'X-ray',
          'RASH_HUMAN_Bandaru2016_unregulated':'X-ray',
          'SUMO1_HUMAN_Roth2017_screenscore':'X-ray',
          'UBC9_HUMAN_Roth2017_screenscore':'X-ray',
          'B3VI55_LIPST_Klesmith2015_SelectionOne':'X-ray',
          'B3VI55_LIPSTSTABLE_Klesmith2015_SelectionTwo':'X-ray',
          'TRPC_THEMA_Chen2017_fitness':'X-ray',
          'TPMT_HUMAN_Matreyek2019_score':'X-ray',
          'P84126_THETH_Chen2017_fitness':'X-ray',
          'MK01_HUMAN_Brenan2016_DOX_Average':'X-ray',

          'PTEN_HUMAN_Matreyek2019_score':'AF',
          'GAL4_YEAST_Shendure2015-SEL_C_40h':'AF',#AF
          'HSP82_YEAST_Bolon2016-selection_coefficient':'AF',#AF
          'IF1_ECOLI_Kelsic2016_fitness_rich_NMR':'NMR',
          'IF1_ECOLI_Kelsic2016_fitness_rich_AF':'AF',
          'BRCA1_HUMAN_Fields2015-e3_NMR':'NMR',
          'BRCA1_HUMAN_Fields2015-e3_AF':'AF',
          'BRCA1_HUMAN_Fields2015-y2h_NMR':'NMR',
          'BRCA1_HUMAN_Fields2015-y2h_AF':'AF',
          'UBE4B_MOUSE_Klevit2013-nscor_log2_ratio_single_NMR':'NMR',
          'PABP_YEAST_Fields2013-linear':'EM',#EM

          }
STUCTURE_RESOLUTION={
          'GFP_AEQVI_Sarkisyan2016':0.9,
          'GB1_Olson2014_ddg':2.07,
          'KKA2_KLEPN_Mikkelsen2014-Kan18_avg':2.1,
          'BLAT_ECOLX_Ostermeier2014-linear':0.85,
          'BLAT_ECOLX_Tenaillon2013-singles-MIC_score':0.85,
          'BLAT_ECOLX_Palzkill2012-ddG_stat':0.85,
          'BLAT_ECOLX_Ranganathan2015-2500':0.85,
          'DLG4_RAT_Ranganathan2012-CRIPT':1.54,
          'YAP1_HUMAN_Fields2012-singles-linear':1.6,
          'RL401_YEAST_Bolon2013-selection_coefficient':1.5,
          'RL401_YEAST_Bolon2014-react_rel':1.5,
          'RL401_YEAST_Mavor2016_DMSO':1.5,
          'MTH3_HAEAESTABILIZED_Tawfik2015-Wrel_G17_filtered':2.8,
          'AMIE_PSEAE_Wrenbeck2017_isobutyramide_normalized_fitness':1.25,
          'CALM1_HUMAN_Roth2017_screenscore':1.7,
          'TRPC_SULSO_Chen2017_fitness':2.,
          'TPK1_HUMAN_Roth2017_screenscore':1.8,
          'RASH_HUMAN_Bandaru2016_unregulated':1.54,
          'SUMO1_HUMAN_Roth2017_screenscore':1.4,
          'UBC9_HUMAN_Roth2017_screenscore':2.8,
          'B3VI55_LIPST_Klesmith2015_SelectionOne':1.5,
          'B3VI55_LIPSTSTABLE_Klesmith2015_SelectionTwo':1.5,
          'TRPC_THEMA_Chen2017_fitness':2.,
          'TPMT_HUMAN_Matreyek2019_score':1.58,
          'P84126_THETH_Chen2017_fitness':1.8,
          'MK01_HUMAN_Brenan2016_DOX_Average':2.,

          'PTEN_HUMAN_Matreyek2019_score':None,
          'GAL4_YEAST_Shendure2015-SEL_C_40h':None,#AF
          'HSP82_YEAST_Bolon2016-selection_coefficient':None,#AF
          'IF1_ECOLI_Kelsic2016_fitness_rich_NMR':None,
          'IF1_ECOLI_Kelsic2016_fitness_rich_AF':None,
          'BRCA1_HUMAN_Fields2015-e3_NMR':None,
          'BRCA1_HUMAN_Fields2015-e3_AF':None,
          'BRCA1_HUMAN_Fields2015-y2h_NMR':None,
          'BRCA1_HUMAN_Fields2015-y2h_AF':None,
          'UBE4B_MOUSE_Klevit2013-nscor_log2_ratio_single_NMR':None,
          'PABP_YEAST_Fields2013-linear':'EM4.8',#EM
          }
def software_path():
    vmd_path = '/mnt/ufs18/home-015/qiuyuchi/software/vmd-1.9.4a54/bin/'
    jackal_path = '/mnt/ufs18/home-015/qiuyuchi/software/jackal/'
    HERMES_path='/mnt/ufs18/home-015/qiuyuchi/software/HERMES/build/'

    path={'vmd_path':vmd_path,'jackal_path':jackal_path,'HERMES_path':HERMES_path}
    return path
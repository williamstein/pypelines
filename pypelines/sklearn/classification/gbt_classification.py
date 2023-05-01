from ..model_base import SklearnModelBase, SklearnModelComparisonBase

gbt_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'learning_rate', 'min': 0, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'n_estimators', 'min': 100, 'max': 10000, 'step': 100},
        {'checked': True, 'name': 'subsample', 'min': 0.1, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'max_depth', 'min': 1, 'max': 10000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'loss', 'selected': ['log_loss'], 'values': ['log_loss', 'deviance', 'exponential']},
    ]
}


class GBTClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'GradientBoostingClassifier()'
        imports = '''from sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('gbt_classifier', model_string, gbt_classification_hyperparams, imports,model_type)

class GBTClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'GradientBoostingClassifier()'
        imports = '''from sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('gbt_classifier', model_string, gbt_classification_hyperparams, imports,model_type)
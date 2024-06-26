from .hau_importer import *

class CollectData():
    def __init__(self, user):
        self.data = {}
        self.user_api(user['MaGV'])
        self.username_MGV = user['MaGV']
        
        self.init_folders()

    def init_folders(self):
        self.DATASETS_PATH = f'.\\{self.username_MGV}_datasets'
        self.RESULTS_PATH = f'.\\{self.username_MGV}_results'
        self.STATISTIC_PATH = f'.\\{self.username_MGV}_statistics'
        self.MODEL_DIR = f'.\\{self.username_MGV}_models'

        if not os.path.exists(self.DATASETS_PATH):
            os.makedirs(self.DATASETS_PATH)

        if not os.path.exists(self.MODEL_DIR):
            os.makedirs(self.MODEL_DIR)

        if not os.path.exists(self.STATISTIC_PATH):
            os.makedirs(self.STATISTIC_PATH)

        if not os.path.exists(self.RESULTS_PATH):
            os.makedirs(self.RESULTS_PATH)

    def collect_data(self, source):
        try:
            with open(source, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except:
            print("No data found!")
    
    def check_user(username, password):
        user_checked = {}
        try:
            user_checked = requests.get(HauSettings.BASE_URL + f"/giaovien/logging/{username}/{password}").json()
            return CollectData(user_checked)
        except:
            print("Something incorrected!")
        return None
    
    def check_admin(username, password):
        admin_checked = {}
        try:
            admin_checked = requests.get(HauSettings.BASE_URL + f"/admin/logging/{username}/{password}").json()
            return admin_checked
        except:
            print("Something incorrected!")
        return None
    
    # def update_api(self, malop):
    #     requests.get(HauSettings.BASE_URL + f"/giaovien/baocao/{malop}")
    
    def user_api(self, username):
        api = requests.get(HauSettings.BASE_URL + f"/giaovien/login_success/{username}").json()
        with open(HauSettings.API_SOURCE, "w", encoding='utf-8') as outfile:
            json.dump(api, outfile,ensure_ascii=False)
        self.collect_data(HauSettings.API_SOURCE)
    
    def get_msv(self):
        list_sv = []
        try:
            for s in self.data['sinhvien']:
                list_sv.append(s['MaSV'])
        except:
            print("No data found in get_msv!")
        return list_sv

    def get_msv_by_malop(self, class_id):
        list_msv = []
        try:
            for item in self.data['dslop']:
                if item['MaLop'] == class_id:
                    list_msv.append(item['MaSV'])
        except:
            print("No data found in get_msv_by_malop!")
        return list_msv
    
    def get_malop(self):
        list_malop = []
        try:
            for item in self.data['lophoc']:
                list_malop.append(item['MaLop'])
        except:
            print("No data found in get_malop!")
        return list_malop
    
    # def check_malop(self, ma_lop):
    #     list_malop = self.get_malop()
    #     if ma_lop in list_malop:
    #         return True
    #     return False
    
    def get_sv_by_malop(self, class_id):
        dssv = []
        try:
            dsmsv = []
            for item in self.data['dslop']:
                if item['MaLop'] == class_id:
                    dsmsv.append(item['MaSV'])
            for item in self.data['sinhvien']:
                if item['MaSV'] in dsmsv:
                    dssv.append(item)
        except:
            print("No data found in get_sv_by_malop!")
        return dssv
    
    def get_baocao_by_malop(self, class_id):
        dssv = []
        try:
            for item in self.data['baocao_all']:
                if item['MaLop'] == class_id:
                    dssv.append(item)
        except:
            print("No data found in get_baocao_by_malop!")
        return dssv
    
    def get_baocao_detail(self, class_id, student_id):
        dssv = []
        try:
            for item in self.data['baocao_detail']:
                if item['MaLop'] == class_id and item['MaSV'] == student_id:
                    dssv.append(item)
        except:
            print("No data found in get_baocao_detail!")
        return dssv

    def get_sv_by_msv(self, msv):
        try:
            for sv in self.data['sinhvien']:
                if sv['MaSV'] == msv:
                    return sv
        except:
            print("No data found in get_sv_by_msv!")
            return {}
        
    def get_ds_by_malop(self):
        ds_malop = []
        try:
            for lop in self.data['lophoc']:
                ds_malop.append(lop['MaLop'])
        except:
            print("No data found in get_ds_by_malop!")
        return ds_malop
            

from pymatgen import MPRester
from side_fxn import _align
import numpy as np
import time


def load_data_from_api(api_key, ele_confine):
    # count loaded data
    select_ = 0
    notselect_ = 0
    nomaterial_ = 0
    save_a_txt_list = []
    # param X
    tt_i_list = []
    # param Y
    a = []
    b = []
    c = []
    alpha = []
    beta = []
    gamma = []

    #####
    # load
    with MPRester(api_key) as m:
        data_ = m.get_materials_ids(ele_confine)  # 鉀鈣鈧鈦釩鉻錳鐵鈷鎳Ca-Co-Cr-Fe-K-Mn-Ni-Sc-Ti-V-
        # 鹼土族Ba-Be-Ca-Mg-Sr-
        print(f"#: {len(data_)}")

        for num, id_ in enumerate(data_):
            try:
                # get whole doc
                data_mat = m.get_doc(f"{id_}")
                decompose_ = data_mat['decomposes_to']
                full_formula_ = data_mat['full_formula']
                nelements_ = data_mat['nelements']
                if decompose_ is None and nelements_ == 2:
                    print(_align((f"{num}.", 5), (f"[Selected]", 20), (f"{id_}", 15), (f"{full_formula_}", 15)))
                    select_ += 1

                    # load X
                    xrd = data_mat['xrd']
                    xrd_Cu = xrd['Cu']
                    xrd_Cu_pat = xrd_Cu['pattern']
                    theta_180_list = {tt: [] for tt in range(180)}
                    for the_info in xrd_Cu_pat:
                        data_tt = int(the_info[2])
                        theta_180_list[data_tt].append(the_info[0])
                    for tt in theta_180_list:
                        if theta_180_list[tt] == []:
                            theta_180_list[tt] = 0
                        else:
                            theta_180_list[tt] = sum(theta_180_list[tt]) / len(theta_180_list[tt])
                    tt_i_list.append(list(theta_180_list.values()))

                    # load Y
                    lattice_ = data_mat['initial_structure']['lattice']
                    a.append(lattice_['a'])
                    b.append(lattice_['b'])
                    c.append(lattice_['c'])
                    alpha.append(lattice_['alpha'])
                    beta.append(lattice_['beta'])
                    gamma.append(lattice_['gamma'])

                    # save a txt
                    save_a_txt_list.append(
                        _align((f"{id_}", 15), (f"{full_formula_}", 15)))

                else:
                    # not selected
                    print(_align((f"{num}.", 5), (f"[Not Selected]", 20), (f"{id_}", 15), (f"{full_formula_}", 15)))
                    notselect_ += 1

            except:
                # no material
                print(_align((f"{num}.", 5), (f"[No material]", 20), (f"{id_}", 15), ("", 1)))
                nomaterial_ += 1
    #####
    # save a sheet
    with open("data_0509.txt", 'w') as f:
        f.write("\n".join(save_a_txt_list))

    return (select_, notselect_, nomaterial_), tt_i_list, a, b, c, alpha, beta, gamma


def get_XY(tt_i_list, a, b, c, alpha, beta, gamma):
    #####
    # X
    tt_i_ar = np.array(tt_i_list)
    X = tt_i_ar

    #####
    # Y
    a_ar = np.array(a)
    b_ar = np.array(b)
    c_ar = np.array(c)
    alpha_ar = np.array(alpha)
    beta_ar = np.array(beta)
    gamma_ar = np.array(gamma)
    Y = np.stack((a_ar, b_ar, c_ar, alpha_ar, beta_ar, gamma_ar), axis=-1)

    return X, Y

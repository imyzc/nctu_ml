import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from joblib import dump, load
from sklearn.svm import SVR
from sklearn.manifold import Isomap
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from _tmp import train_sizes_h, train_score_h, test_score_h, train_score_h_mean, test_score_h_mean, train_sizes_r, train_score_r, test_score_r, train_score_r_mean, test_score_r_mean

def train_ploting():
    plt.figure(figsize=(10, 5))
    plt.subplots_adjust(wspace=0.5, hspace=0)
    plt.subplot(1,2,1)
    plt.title('Height training')
    plt.plot(train_sizes_h, train_score_h_mean, 'o-', label="Training score")
    plt.plot(train_sizes_h, test_score_h_mean, 'o-', label="Cross-validation score")
    plt.xlabel("Training examples")
    plt.ylabel("score")
    plt.legend(loc="best")
    #plt.xlim(5, 10000)
    plt.xscale('symlog')
    plt.grid(True)
    plt.gca().xaxis.grid(True, which='minor') 
    #plt.ylim(0, 1.05)
    plt.subplot(1,2,2)
    plt.title('Distance training')
    plt.plot(train_sizes_r, train_score_r_mean, 'o-', label="Training score")
    plt.plot(train_sizes_r, test_score_r_mean, 'o-', label="Cross-validation score")
    plt.xlabel("Training examples")
    plt.ylabel("score")
    plt.legend(loc="best")
    #plt.xlim(5, 10000)
    plt.xscale('symlog')
    plt.grid(True)
    plt.gca().xaxis.grid(True, which='minor') 
    #plt.ylim(0, 1.05)
    plt.show()

def data_ploting_parameter(ab, cd, ef, gh, ij):
    vp = np.random.uniform(ab, cd, ij)
    tp = np.random.uniform(ef, gh, ij)
    hp = (vp*np.sin(tp*(np.pi/180)))**2/19.6
    rp = (vp**2)*np.sin(2*tp*(np.pi/180))/9.8
    vptp = np.stack((vp, tp), axis = -1)
    from _tmp import X, y, model_h, model_r, model_h_path, model_r_path
    model_h.fit(X, y[:,-2])
    model_r.fit(X, y[:,-1])
    dump(model_h, model_h_path)
    dump(model_r, model_r_path)
    model_h.predict(vptp)
    model_r.predict(vptp)
    from _tmp import v, theta, h, r
    fig = plt.figure(figsize=(6, 6))
    ax = fig.gca(projection='3d')
    ax.scatter(v[:500], theta[:500], h[:500], c=h[:500], cmap=cm.coolwarm)
    ax.scatter(vp, tp, model_h.predict(vptp), c='r',marker='x')
    ax.scatter(vp, tp, hp, c='g',marker='^')
    ax.text2D(0.05, 0.95, 'height', transform=ax.transAxes)
    ax.set_xlabel('velocity')
    ax.set_ylabel('theta')
    ax.set_zlabel('height')
    plt.show()
    fig = plt.figure(figsize=(6, 6))
    ax = fig.gca(projection='3d')
    ax.scatter(v[:500], theta[:500], r[:500], c=r[:500], cmap=cm.coolwarm)
    ax.scatter(vp, tp, model_r.predict(vptp), c='r',marker='x')
    ax.scatter(vp, tp, rp, c='g',marker='^')
    ax.text2D(0.05, 0.95, 'Distance', transform=ax.transAxes)
    ax.set_xlabel('velocity')
    ax.set_ylabel('theta')
    ax.set_zlabel('distance')
    plt.show()
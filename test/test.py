import pickle
resources_web_app = pickle.load(open('resources/resources_web_app.pickle', 'rb'))
print(resources_web_app['columns_to_plot_people_dependent'])
print(resources_web_app['columns_to_plot_non_people_dependent_barplot'] )
import matplotlib
    
def plot_raw_data_type(fig, data_dict, file_name, time_index, data_type_index, \
      plot_title, y_label):
    fig.clf()
    
    x_plot = fig.add_subplot(3,1,1)
    y_plot = fig.add_subplot(3,1,2)
    z_plot = fig.add_subplot(3,1,3)
    
    x_plot.plot(
        data_dict[file_name][:,time_index], 
        data_dict[file_name][:,data_type_index]
    )
    y_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,data_type_index + 1]
    )
    z_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,data_type_index + 2]
    )
    
    _format_plot(x_plot, plot_title + " - X axis", "Time (s)", y_label, False)
    _format_plot(y_plot, plot_title + " - Y axis", "Time (s)", y_label, False)
    _format_plot(z_plot, plot_title + " - Z axis", "Time (s)", y_label, False)
    fig.show()
    
def plot_filtered_data(fig, data_dict, file_name, time_index, quat_index, \
      tait_bryan_index, plot_title):
    fig.clf()
    
    quat_plot = fig.add_subplot(2,1,1)
    tait_bryan_plot = fig.add_subplot(2,1,2)
    
    quat_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,quat_index],
        label = "Qw"
    )
    quat_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,quat_index + 1],
        label = "Qx"
    )
    quat_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,quat_index + 2],
        label = "Qy"
    )
    quat_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,quat_index + 3],
        label = "Qz"
    )
    
    tait_bryan_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,tait_bryan_index],
        label = "Roll"
    )
    tait_bryan_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,tait_bryan_index + 1],
        label = "Pitch"
    )
    tait_bryan_plot.plot(
        data_dict[file_name][:,time_index],
        data_dict[file_name][:,tait_bryan_index + 2],
        label = "Yaw"
    )

    _format_plot(
        quat_plot, 
        plot_title + " - Quaternion Orientation", 
        "Time (s)", "Vector Magnitude (norm)",
        True
    )
    _format_plot(
        tait_bryan_plot, 
        plot_title + " - Tait-Bryan Angles", 
        "Time (s)", "Rotation (rad)",
        True
    )

# Helper functions
def _format_plot(plot, title, x_label, y_label, has_legend):
    # Add titles
    plot.set_title(title)
    plot.set_xlabel(x_label)
    plot.set_ylabel(y_label) 
    # Shrink current axis's height
    box = plot.get_position()
    plot.set_position([box.x0, box.y0 + box.height * 0.2,
                         box.width, box.height * 0.8])
    if has_legend:
        # Put a legend below current axis
        plot.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
                  fancybox=True, shadow=True, ncol=4)
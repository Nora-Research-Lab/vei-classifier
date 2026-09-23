def classify(column_height_km, volume_km3, duration_hours):
    """
    Classify volcanic eruption VEI according to Newhall & Self (1982).
    Parameters:
        column_height_km : float (0-50)
        volume_km3       : float (0-1000)
        duration_hours   : float (0-48)
    Returns:
        (integer VEI, string eruption type)
    """
    # Input validation
    if column_height_km < 0 or volume_km3 < 0 or duration_hours < 0:
        raise ValueError("Input values must be non-negative.")
    
    # Convert volume to m³
    volume_m3 = volume_km3 * 1e9  # 1 km³ = 1e9 m³
    
    # Determine VEI from column height (km)
    height_vei = 0
    if column_height_km < 0.1:
        height_vei = 0
    elif column_height_km < 1:
        height_vei = 1
    elif column_height_km < 5:
        height_vei = 2
    elif column_height_km < 15:
        height_vei = 3
    elif column_height_km < 25:
        height_vei = 4
    else:
        height_vei = 5  # above 25 km, but VEI may be higher based on volume
    
    # Determine VEI from volume (m³)
    volume_vei = 0
    if volume_m3 < 1e4:
        volume_vei = 0
    elif volume_m3 < 1e6:
        volume_vei = 1
    elif volume_m3 < 1e7:
        volume_vei = 2
    elif volume_m3 < 1e8:
        volume_vei = 3
    elif volume_m3 < 1e9:
        volume_vei = 4
    elif volume_m3 < 1e10:
        volume_vei = 5
    elif volume_m3 < 1e11:
        volume_vei = 6
    elif volume_m3 < 1e12:
        volume_vei = 7
    else:
        volume_vei = 8
    
    # Determine VEI from duration (hours)
    dur_vei = 0
    if duration_hours < 1:
        dur_vei = 0
    elif duration_hours < 6:
        dur_vei = 1
    elif duration_hours < 12:
        dur_vei = 2
    elif duration_hours < 24:
        dur_vei = 3
    elif duration_hours < 48:
        dur_vei = 4
    else:
        dur_vei = 5  # 48+ hours, only used up to VEI 5
        # For VEI >=6, duration is not considered (assumed duration less relevant)
    # According to spec: duration not used for VEI >=6, so cap dur_vei at 5
    if dur_vei > 5:
        dur_vei = 5
    
    # Final VEI = maximum of the three parameter-specific VEIs
    vei = max(height_vei, volume_vei, dur_vei)
    
    # Map VEI to eruption type
    if vei <= 1:
        eruption_type = "Hawaiian / Strombolian"
    elif vei <= 3:
        eruption_type = "Vulcanian"
    elif vei <= 5:
        eruption_type = "Plinian"
    elif vei <= 7:
        eruption_type = "Ultra-Plinian"
    else:
        eruption_type = "Supervolcanic"
    
    return vei, eruption_type

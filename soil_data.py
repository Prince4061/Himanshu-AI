# =============================================================================
# Himanshu AI - Regional Soil Profile Data
# =============================================================================
# Pre-loaded soil data for major Indian agricultural regions.
# This data is sent as context to the AI so it can make better diagnoses
# based on the local soil conditions.
# =============================================================================

SOIL_PROFILES = {
    "Punjab": {
        "region": "Punjab",
        "soil_type": "Alluvial Soil (Jalodh Mitti)",
        "ph_level": "7.5 - 8.5 (Slightly Alkaline)",
        "organic_carbon": "0.4% - 0.6% (Medium)",
        "nitrogen": "Low to Medium (180-280 kg/ha)",
        "phosphorus": "Medium (15-25 kg/ha)",
        "potassium": "High (250-350 kg/ha)",
        "zinc": "Deficient in many areas",
        "iron": "Low in alkaline soils",
        "moisture_level": "Moderate to High (canal irrigation)",
        "climate": "Semi-arid, Hot summers (45°C), Cold winters (0°C)",
        "rainfall": "500-700 mm annually",
        "major_crops": ["Wheat (Gehun)", "Rice (Chawal)", "Cotton (Kapas)", "Sugarcane (Ganna)", "Maize (Makka)"],
        "common_problems": ["Soil salinity", "Waterlogging", "Zinc deficiency", "Stubble burning effects"],
        "water_table": "Declining in central Punjab, rising in southwest"
    },
    "Haryana": {
        "region": "Haryana",
        "soil_type": "Alluvial & Sandy Loam (Retili Domat)",
        "ph_level": "7.8 - 8.8 (Alkaline)",
        "organic_carbon": "0.3% - 0.5% (Low to Medium)",
        "nitrogen": "Low (150-250 kg/ha)",
        "phosphorus": "Medium (12-22 kg/ha)",
        "potassium": "Medium to High (200-300 kg/ha)",
        "zinc": "Widely deficient",
        "iron": "Deficient in sandy areas",
        "moisture_level": "Low to Moderate",
        "climate": "Semi-arid to Arid, Extreme temperatures",
        "rainfall": "300-550 mm annually",
        "major_crops": ["Wheat (Gehun)", "Rice (Chawal)", "Mustard (Sarson)", "Bajra", "Cotton (Kapas)"],
        "common_problems": ["Salinity/Sodicity", "Low organic matter", "Water scarcity", "Sand dune encroachment"],
        "water_table": "Critically low in southern Haryana"
    },
    "Uttar Pradesh": {
        "region": "Uttar Pradesh",
        "soil_type": "Alluvial Soil (Gangetic Plains - Jalodh Mitti)",
        "ph_level": "7.0 - 8.5 (Neutral to Alkaline)",
        "organic_carbon": "0.3% - 0.7% (Low to Medium)",
        "nitrogen": "Low to Medium (200-300 kg/ha)",
        "phosphorus": "Low to Medium (10-20 kg/ha)",
        "potassium": "Medium (180-280 kg/ha)",
        "zinc": "Deficient in many districts",
        "iron": "Generally adequate",
        "moisture_level": "High in eastern UP, moderate in western UP",
        "climate": "Subtropical, Hot humid summers, Cool dry winters",
        "rainfall": "600-1100 mm annually",
        "major_crops": ["Wheat (Gehun)", "Rice (Chawal)", "Sugarcane (Ganna)", "Potato (Aloo)", "Mustard (Sarson)", "Pulses (Dal)"],
        "common_problems": ["Usar (sodic) soils", "Flood damage in eastern region", "Nutrient depletion", "Over-irrigation"],
        "water_table": "Variable - high in east, declining in west"
    },
    "Maharashtra": {
        "region": "Maharashtra",
        "soil_type": "Black Cotton Soil (Kali Mitti / Regur) & Laterite",
        "ph_level": "6.5 - 8.0 (Slightly Acidic to Alkaline)",
        "organic_carbon": "0.4% - 0.8% (Medium)",
        "nitrogen": "Low (150-250 kg/ha)",
        "phosphorus": "Low to Medium (8-18 kg/ha)",
        "potassium": "High (280-400 kg/ha)",
        "zinc": "Deficient in Vidarbha",
        "iron": "Adequate in laterite areas",
        "moisture_level": "Low to Moderate (rainfed areas)",
        "climate": "Tropical, Hot and dry, Monsoon dependent",
        "rainfall": "500-3000 mm (varies greatly: Konkan vs Marathwada)",
        "major_crops": ["Cotton (Kapas)", "Soybean", "Sugarcane (Ganna)", "Jowar", "Grapes (Angoor)", "Onion (Pyaaz)"],
        "common_problems": ["Drought stress in Marathwada", "Soil cracking", "Low nitrogen", "Bollworm in cotton"],
        "water_table": "Very low in Marathwada and Vidarbha"
    },
    "Madhya Pradesh": {
        "region": "Madhya Pradesh",
        "soil_type": "Black Soil (Kali Mitti) & Red-Yellow Soil (Lal-Peeli)",
        "ph_level": "6.5 - 8.0",
        "organic_carbon": "0.4% - 0.6% (Medium)",
        "nitrogen": "Low (160-260 kg/ha)",
        "phosphorus": "Low (8-15 kg/ha)",
        "potassium": "High (250-350 kg/ha)",
        "zinc": "Deficient",
        "iron": "Adequate",
        "moisture_level": "Moderate (monsoon dependent)",
        "climate": "Subtropical, Hot summers, Mild winters",
        "rainfall": "800-1400 mm annually",
        "major_crops": ["Soybean (Soya)", "Wheat (Gehun)", "Gram (Chana)", "Rice (Chawal)", "Cotton (Kapas)", "Maize (Makka)"],
        "common_problems": ["Soil erosion", "Low phosphorus", "Terminal drought", "Poor drainage in black soils"],
        "water_table": "Moderate, declining in Malwa plateau"
    },
    "Rajasthan": {
        "region": "Rajasthan",
        "soil_type": "Desert Sandy Soil (Registan Mitti) & Aridisol",
        "ph_level": "8.0 - 9.5 (Highly Alkaline)",
        "organic_carbon": "0.1% - 0.3% (Very Low)",
        "nitrogen": "Very Low (100-180 kg/ha)",
        "phosphorus": "Low (5-12 kg/ha)",
        "potassium": "Medium (150-250 kg/ha)",
        "zinc": "Severely deficient",
        "iron": "Deficient",
        "moisture_level": "Very Low",
        "climate": "Arid to Semi-arid, Extreme heat (50°C), Cold nights in winter",
        "rainfall": "100-500 mm annually",
        "major_crops": ["Bajra", "Moong", "Moth", "Guar", "Mustard (Sarson)", "Wheat (Gehun)", "Cumin (Jeera)"],
        "common_problems": ["Extreme water scarcity", "Sand storms", "Soil salinity", "Very low fertility", "Wind erosion"],
        "water_table": "Critically low, over-exploited"
    },
    "Bihar": {
        "region": "Bihar",
        "soil_type": "Alluvial Soil (Gangetic Flood Plain - Jalodh)",
        "ph_level": "6.5 - 7.8 (Neutral to Slightly Alkaline)",
        "organic_carbon": "0.4% - 0.7% (Medium)",
        "nitrogen": "Medium (250-350 kg/ha)",
        "phosphorus": "Low to Medium (10-18 kg/ha)",
        "potassium": "Low to Medium (150-250 kg/ha)",
        "zinc": "Deficient in calcareous soils",
        "iron": "Generally adequate",
        "moisture_level": "High (flood prone)",
        "climate": "Subtropical, Humid, Hot summers, Mild winters",
        "rainfall": "1000-1500 mm annually",
        "major_crops": ["Rice (Chawal)", "Wheat (Gehun)", "Maize (Makka)", "Litchi", "Makhana", "Potato (Aloo)"],
        "common_problems": ["Annual flooding", "Waterlogging in north Bihar", "Soil erosion", "Sand deposition from floods"],
        "water_table": "High, rising in many areas"
    },
    "Tamil Nadu": {
        "region": "Tamil Nadu",
        "soil_type": "Red Soil (Lal Mitti), Laterite & Coastal Alluvial",
        "ph_level": "5.5 - 7.5 (Acidic to Neutral)",
        "organic_carbon": "0.3% - 0.6% (Low to Medium)",
        "nitrogen": "Low (150-250 kg/ha)",
        "phosphorus": "Medium (12-20 kg/ha)",
        "potassium": "Medium (180-280 kg/ha)",
        "zinc": "Deficient in red soil areas",
        "iron": "Adequate to high",
        "moisture_level": "Variable (monsoon dependent)",
        "climate": "Tropical, Hot and humid, NE monsoon dominant",
        "rainfall": "700-1200 mm annually (NE monsoon: Oct-Dec)",
        "major_crops": ["Rice (Chawal)", "Banana (Kela)", "Coconut (Nariyal)", "Sugarcane (Ganna)", "Cotton (Kapas)", "Groundnut (Moongfali)"],
        "common_problems": ["Soil acidity in highlands", "Coastal salinity", "Low organic matter", "Cyclone damage"],
        "water_table": "Low in many districts, over-extraction"
    },
    "West Bengal": {
        "region": "West Bengal",
        "soil_type": "Alluvial (Gangetic Delta) & Laterite (Red Soil)",
        "ph_level": "5.5 - 7.5 (Acidic to Neutral)",
        "organic_carbon": "0.5% - 0.9% (Medium to High)",
        "nitrogen": "Medium (250-350 kg/ha)",
        "phosphorus": "Low to Medium (8-18 kg/ha)",
        "potassium": "Medium (180-280 kg/ha)",
        "zinc": "Deficient in some areas",
        "iron": "High in laterite areas (toxicity risk)",
        "moisture_level": "High",
        "climate": "Tropical, Hot and humid, Heavy monsoon",
        "rainfall": "1200-2500 mm annually",
        "major_crops": ["Rice (Chawal)", "Jute (Pat)", "Tea (Chai)", "Potato (Aloo)", "Vegetables", "Mango (Aam)"],
        "common_problems": ["Waterlogging", "Iron toxicity in laterite soils", "Acidity", "Cyclone and flood damage"],
        "water_table": "High, saline in Sundarbans"
    },
    "Gujarat": {
        "region": "Gujarat",
        "soil_type": "Black Soil (Kali Mitti), Sandy & Coastal Saline",
        "ph_level": "7.0 - 8.8 (Neutral to Alkaline)",
        "organic_carbon": "0.3% - 0.6% (Low to Medium)",
        "nitrogen": "Low (150-250 kg/ha)",
        "phosphorus": "Medium (12-22 kg/ha)",
        "potassium": "Medium to High (200-350 kg/ha)",
        "zinc": "Deficient in Kutch and Saurashtra",
        "iron": "Deficient in calcareous soils",
        "moisture_level": "Low to Moderate",
        "climate": "Arid to Semi-arid, Hot and dry",
        "rainfall": "300-1500 mm (varies: Kutch vs South Gujarat)",
        "major_crops": ["Cotton (Kapas)", "Groundnut (Moongfali)", "Wheat (Gehun)", "Bajra", "Tobacco", "Cumin (Jeera)"],
        "common_problems": ["Soil salinity in Kutch", "Water scarcity", "Fluoride contamination", "Wind erosion in Kutch"],
        "water_table": "Low in Saurashtra and Kutch"
    },
    "Karnataka": {
        "region": "Karnataka",
        "soil_type": "Red Soil (Lal Mitti), Laterite & Black Soil",
        "ph_level": "5.5 - 7.8 (Acidic to Slightly Alkaline)",
        "organic_carbon": "0.4% - 0.7% (Medium)",
        "nitrogen": "Low to Medium (180-300 kg/ha)",
        "phosphorus": "Low (8-15 kg/ha)",
        "potassium": "Medium (180-280 kg/ha)",
        "zinc": "Deficient",
        "iron": "Adequate in laterite, low in black soil areas",
        "moisture_level": "Variable",
        "climate": "Tropical, Moderate to hot",
        "rainfall": "500-3000 mm (varies: dry north vs wet coast)",
        "major_crops": ["Ragi", "Rice (Chawal)", "Jowar", "Coffee", "Arecanut (Supari)", "Sugarcane (Ganna)", "Silk (Resham)"],
        "common_problems": ["Drought in north Karnataka", "Soil erosion in Western Ghats", "Low phosphorus", "Fluoride in groundwater"],
        "water_table": "Low in north, adequate in coastal areas"
    },
    "Andhra Pradesh & Telangana": {
        "region": "Andhra Pradesh & Telangana",
        "soil_type": "Red Soil (Lal Mitti), Black Cotton Soil & Coastal Alluvial",
        "ph_level": "6.0 - 8.0",
        "organic_carbon": "0.3% - 0.6% (Low to Medium)",
        "nitrogen": "Low (150-250 kg/ha)",
        "phosphorus": "Low (8-15 kg/ha)",
        "potassium": "Medium to High (200-350 kg/ha)",
        "zinc": "Deficient",
        "iron": "Variable",
        "moisture_level": "Low to Moderate",
        "climate": "Tropical, Hot and dry, Cyclone-prone coast",
        "rainfall": "600-1200 mm annually",
        "major_crops": ["Rice (Chawal)", "Cotton (Kapas)", "Chili (Mirchi)", "Turmeric (Haldi)", "Mango (Aam)", "Tobacco"],
        "common_problems": ["Drought in Rayalaseema", "Fluoride contamination", "Soil erosion", "Cyclone damage in coastal areas"],
        "water_table": "Low in Telangana plateau"
    }
}


def get_soil_profile(region_name):
    """
    Get soil profile data for a given region.
    Returns a formatted string with all soil information.
    """
    profile = SOIL_PROFILES.get(region_name)
    if not profile:
        return f"Region '{region_name}' ka soil data available nahi hai."

    soil_info = f"""
=== SOIL PROFILE: {profile['region']} ===
🌍 Soil Type: {profile['soil_type']}
📊 pH Level: {profile['ph_level']}
🧪 Organic Carbon: {profile['organic_carbon']}
💧 Moisture Level: {profile['moisture_level']}

--- NUTRIENTS ---
🟢 Nitrogen (N): {profile['nitrogen']}
🟡 Phosphorus (P): {profile['phosphorus']}
🔵 Potassium (K): {profile['potassium']}
⚪ Zinc (Zn): {profile['zinc']}
🟤 Iron (Fe): {profile['iron']}

--- CLIMATE ---
🌤️ Climate: {profile['climate']}
🌧️ Rainfall: {profile['rainfall']}
💧 Water Table: {profile['water_table']}

--- CROPS & ISSUES ---
🌾 Major Crops: {', '.join(profile['major_crops'])}
⚠️ Common Problems: {', '.join(profile['common_problems'])}
"""
    return soil_info


def get_all_regions():
    """Return list of all available region names."""
    return list(SOIL_PROFILES.keys())

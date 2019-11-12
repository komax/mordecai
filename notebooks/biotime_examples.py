
biotime_sample_sites = {
    "Anderson et al. - 2011": "This historical data set consists of 44 permanent 1-m 2 quadrats located on northern mixed prairie in Miles City, Montana, USA.",
    "Farah et al. - 2014": "The municipal reserve of Santa Genebra (MRSG) has a total area of 251.77 ha and constitutes one of the major remnants of Seasonal Semideciduous Forest (a subtype of Atlantic Forest) in the state of São Paulo. It is a fragment isolated from other forests and surrounded by agricultural areas and residential neighborhoods. The local climate is of the Cwa type, defined as hot and humid, with dry winters and hot, rainy summers.",
    "Holmes et al. - 1986": "This study was conducted in the Hubbard Brook Experimental Forest, a 3076-ha sector of the White Mountain National Forest, West Thornton Grafton County, but showed no increasing or decreasing trends over the 16 yr of the study (Fig. 1). Periods of cool, wet weather often occurred during May and early June, while thunderstorms, accompanied by heavy rains, high winds, and sometimes hail, were more common in late June and July.",
    "Rocha et al. - 2017": "Fieldwork was conducted at the BDFFP, located *80 km north of Manaus (2°30 0 S, 60°W), Brazil (see Fig. S1 in the Online Supplementary Material). The area is classified as tropical moist forest, and is characterized by a mosaic of terra firme rainforest, secondary regrowth, and primary forest fragments. Annual rainfall varies from 1900 to 3500 mm, with a dry season between June and October . The forest fragments were isolated from CF by distances of 80-650 m in the early 1980s, and are categorized into size classes of 1, 10 and 100 ha. Each fragment was re-isolated on 3-4 occasions prior to this study, most recently between 1999 and 2001 (Laurance et al. 2011). The matrix is composed of tall secondary forest dominated mainly by Vismia spp. and Cecropia spp.",
    "Thomsen et al. - 2016": "A modified Robinson light trap was installed 17Á5 m above ground at the roof of the Zoological Museum in Copenhagen, Denmark (N 55Á702512°, E 12Á558956°). A 250 W mercury vapour bulb was used as light source. In the trap, 1,1,2,2-tetrachlorethane was used as killing agent. The trap was emptied on an approximately weekly basis and was active from AprilNovember 1992-2009. All individual records of Lepidoptera and Coleoptera were collected, identified to species level and counted yielding qualitative (species) and quantitative (number of individuals within each species) data for the entire study period. All handling and identification of material was carried out consistently throughout the entire period by the same three persons: for Lepidoptera (OK) and Coleoptera (initiated by the late Dr. Michael Hansen and completed by JP). The final data set was subjected to a thorough quality check, and the few records (&lt;20 individual records) that could not be accounted for by comparison of collection periods were discarded. We excluded the first (1992) and the last year (2009) of the data set to minimize start-up effects (operating the trap in a standardized manner comparable to the remainder of the study period) and influence from alteration of the local habitat in 2009. Furthermore, in 1992 and 2009 the trap was not active in the entire season. To account for variation in sampling intervals, we grouped the data set into standardized 10-day periods the first starting on 1st of January (Julian Day 1) and the last period ending on December 26 (Julian Day 360). The 10-day interval is slightly longer than the mean sampling interval of 7 days.",
    "Woods - 2009": "Established in 1935, a regular grid of 256 permanent plots includes about 20% of a 100-ha old-growth forest at the Dukes Research Natural Area in northern Michigan, USA. Woody stems have been re-measured 3-7 times providing extensive quantitative records of population and community dynamics over periods of up to 72 years. Woody stems in upland hemlock-northern hardwood stands, about half of the study plots, have been mapped and individually tracked since about 1990."
}

biotime_sites_from_metadata = {
    "Anderson et al. - 2011": {
        "study_id": 473,
        "cent_latitude": 46.316667,
        "cent_longitude": -105.8 
    },
    "Farah et al. - 2014": {
        "study_id": 322,
        "cent_latitude": -22.825,
        "cent_longitude": -47.1058
    },
    "Holmes et al. - 1986": {
        "study_id": 39,
        "cent_latitude": 43.91,
        "cent_longitude": -71.75
    },
    "Rocha et al. - 2017": {
        "study_id": 516,
        "cent_latitude": -2.386381,
        "cent_longitude": -59.918769
    },
    "Thomsen et al. - 2016": {
        "study_id": 249,
        "cent_latitude": 55.702512,
        "cent_longitude": 12.558956
    },
    "Woods - 2009": {
        "study_id": 255,
        "cent_latitude": 46.3667,
        "cent_longitude": -87.1333
    }
}


def geocoordinates_from_study(key):
    if not key in biotime_sites_from_metadata:
        raise RuntimeError(f'Cannot find study"{key}" in {biotime_sites_from_metadata.keys()}')
    else:
        biotime_entry = biotime_sites_from_metadata[key]
        latitude = biotime_entry["cent_latitude"]
        longitude = biotime_entry["cent_longitude"]
        return latitude, longitude

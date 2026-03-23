"""
Tool functions for the Miami Resources agents.
Google ADK auto-discovers plain Python functions with type hints and docstrings.
"""

from ..data.programs import PROGRAMS, format_program


def search_housing_programs(query: str = "", language: str = "en") -> str:
    """Search for housing assistance programs in Miami-Dade County.

    Args:
        query: Optional search term (e.g. 'section 8', 'shelter', 'rent help').
        language: Response language - 'en' for English, 'es' for Spanish, 'ht' for Haitian Creole.

    Returns:
        Formatted list of matching housing programs with contact details.
    """
    results = [p for p in PROGRAMS if p["category"] == "housing"]
    if query:
        q = query.lower()
        results = [
            p
            for p in results
            if q in p["name"].get(language, p["name"]["en"]).lower()
            or q in p["description"].get(language, p["description"]["en"]).lower()
            or q in p.get("address", "").lower()
        ]
    if not results:
        return _no_results_message(language)
    return "\n\n---\n\n".join(format_program(p, language) for p in results)


def search_food_programs(query: str = "", language: str = "en") -> str:
    """Search for food assistance programs in Miami-Dade County.

    Args:
        query: Optional search term (e.g. 'food stamps', 'food bank', 'WIC', 'meals').
        language: Response language - 'en', 'es', or 'ht'.

    Returns:
        Formatted list of matching food programs with contact details.
    """
    results = [p for p in PROGRAMS if p["category"] == "food"]
    if query:
        q = query.lower()
        results = [
            p
            for p in results
            if q in p["name"].get(language, p["name"]["en"]).lower()
            or q in p["description"].get(language, p["description"]["en"]).lower()
        ]
    if not results:
        return _no_results_message(language)
    return "\n\n---\n\n".join(format_program(p, language) for p in results)


def search_healthcare_programs(query: str = "", language: str = "en") -> str:
    """Search for healthcare programs in Miami-Dade County.

    Args:
        query: Optional search term (e.g. 'medicaid', 'dental', 'mental health', 'clinic').
        language: Response language - 'en', 'es', or 'ht'.

    Returns:
        Formatted list of matching healthcare programs with contact details.
    """
    results = [p for p in PROGRAMS if p["category"] == "healthcare"]
    if query:
        q = query.lower()
        results = [
            p
            for p in results
            if q in p["name"].get(language, p["name"]["en"]).lower()
            or q in p["description"].get(language, p["description"]["en"]).lower()
        ]
    if not results:
        return _no_results_message(language)
    return "\n\n---\n\n".join(format_program(p, language) for p in results)


def search_job_programs(query: str = "", language: str = "en") -> str:
    """Search for job and employment programs in Miami-Dade County.

    Args:
        query: Optional search term (e.g. 'training', 'resume', 'career', 'youth').
        language: Response language - 'en', 'es', or 'ht'.

    Returns:
        Formatted list of matching job programs with contact details.
    """
    results = [p for p in PROGRAMS if p["category"] == "jobs"]
    if query:
        q = query.lower()
        results = [
            p
            for p in results
            if q in p["name"].get(language, p["name"]["en"]).lower()
            or q in p["description"].get(language, p["description"]["en"]).lower()
        ]
    if not results:
        return _no_results_message(language)
    return "\n\n---\n\n".join(format_program(p, language) for p in results)


def search_education_programs(
    query: str = "", language: str = "en", age_group: str = ""
) -> str:
    """Search for education programs in Miami-Dade County.

    Args:
        query: Optional search term (e.g. 'GED', 'college', 'scholarship', 'Head Start').
        language: Response language - 'en', 'es', or 'ht'.
        age_group: Optional filter - 'child', 'teen', 'adult', or empty for all.

    Returns:
        Formatted list of matching education programs with contact details.
    """
    results = [p for p in PROGRAMS if p["category"] == "education"]
    if query:
        q = query.lower()
        results = [
            p
            for p in results
            if q in p["name"].get(language, p["name"]["en"]).lower()
            or q in p["description"].get(language, p["description"]["en"]).lower()
        ]
    if age_group:
        age_filters = {
            "child": ["head-start", "mdcps", "school"],
            "teen": ["mdcps", "bright-futures", "education-fund"],
            "adult": ["mdc", "adult-ed", "pell", "library"],
        }
        ids = age_filters.get(age_group, [])
        if ids:
            results = [
                p for p in results if any(kw in p["id"] for kw in ids)
            ]
    if not results:
        return _no_results_message(language)
    return "\n\n---\n\n".join(format_program(p, language) for p in results)


def check_snap_eligibility(household_size: int, monthly_income: float) -> str:
    """Check if a household may be eligible for SNAP (food stamps) benefits.

    Args:
        household_size: Number of people in the household.
        monthly_income: Total gross monthly household income in dollars.

    Returns:
        Eligibility assessment with next steps.
    """
    # 2024-2025 SNAP gross income limits (200% FPL for Florida broad-based categorical eligibility)
    limits = {
        1: 2_430, 2: 3_288, 3: 4_144, 4: 5_000,
        5: 5_858, 6: 6_714, 7: 7_572, 8: 8_428,
    }
    extra_per_person = 858
    if household_size <= 8:
        limit = limits[household_size]
    else:
        limit = limits[8] + (household_size - 8) * extra_per_person

    if monthly_income <= limit:
        return (
            f"Based on a household of {household_size} with ${monthly_income:,.0f}/month gross income: "
            f"You MAY be eligible for SNAP. The gross income limit is ${limit:,}/month.\n\n"
            f"Apply online at MyACCESS: https://www.myflorida.com/accessflorida/\n"
            f"Or call: 866-762-2237\n\n"
            f"Note: This is an estimate. Final eligibility depends on net income, assets, and other factors."
        )
    else:
        return (
            f"Based on a household of {household_size} with ${monthly_income:,.0f}/month gross income: "
            f"You may exceed the gross income limit of ${limit:,}/month for SNAP.\n\n"
            f"However, you may still qualify based on net income or if you have high deductions "
            f"(medical, shelter, childcare). Apply anyway — the system will assess your full situation.\n\n"
            f"Apply at: https://www.myflorida.com/accessflorida/\n"
            f"Or call: 866-762-2237"
        )


def get_crisis_resources(language: str = "en") -> str:
    """Get emergency and crisis resource phone numbers.

    Args:
        language: Response language - 'en', 'es', or 'ht'.

    Returns:
        List of crisis hotlines and emergency numbers.
    """
    if language == "es":
        return (
            "🚨 **Recursos de Emergencia y Crisis**\n\n"
            "- **Emergencia:** 911\n"
            "- **Línea de Ayuda 211:** Llame 211 o 305-358-4357 (24/7, multilingüe)\n"
            "- **Línea Nacional de Violencia Doméstica:** 1-800-799-7233\n"
            "- **Línea de Prevención del Suicidio:** 988\n"
            "- **Línea de Personas sin Hogar:** 1-877-994-4357\n"
            "- **Línea de Abuso Infantil:** 1-800-962-2873\n"
            "- **Control de Envenenamiento:** 1-800-222-1222\n"
        )
    elif language == "ht":
        return (
            "🚨 **Resous Ijans ak Kriz**\n\n"
            "- **Ijans:** 911\n"
            "- **Liy Èd 211:** Rele 211 oswa 305-358-4357 (24/7, miltilingw)\n"
            "- **Liy Nasyonal Vyolans Domestik:** 1-800-799-7233\n"
            "- **Liy Prevansyon Swisid:** 988\n"
            "- **Liy Sanzabri:** 1-877-994-4357\n"
            "- **Liy Abi Timoun:** 1-800-962-2873\n"
            "- **Kontwòl Pwazonnman:** 1-800-222-1222\n"
        )
    else:
        return (
            "🚨 **Emergency & Crisis Resources**\n\n"
            "- **Emergency:** 911\n"
            "- **211 Helpline:** Call 211 or 305-358-4357 (24/7, multilingual)\n"
            "- **National Domestic Violence Hotline:** 1-800-799-7233\n"
            "- **Suicide & Crisis Lifeline:** 988\n"
            "- **Homeless Helpline:** 1-877-994-4357\n"
            "- **Child Abuse Hotline:** 1-800-962-2873\n"
            "- **Poison Control:** 1-800-222-1222\n"
        )


def _no_results_message(language: str) -> str:
    messages = {
        "en": "No programs found matching your search. Try broadening your search terms, or call 211 for personalized help.",
        "es": "No se encontraron programas que coincidan con su búsqueda. Intente ampliar los términos de búsqueda, o llame al 211 para ayuda personalizada.",
        "ht": "Pa jwenn pwogram ki matche ak rechèch ou. Eseye elaji tèm rechèch ou, oswa rele 211 pou èd pèsonalize.",
    }
    return messages.get(language, messages["en"])

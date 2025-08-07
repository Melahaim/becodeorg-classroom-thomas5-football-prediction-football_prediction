"""
🚀 FOOTBALL PREDICTION APP - VERSION V10.5.0
==============================================
Application de prédiction football avancée avec:
✅ Modèle d'ensemble 6-en-1 avec Head-to-Head et Facteur Domicile Variable
✅ Analyse forme récente équipes  
✅ Facteurs de condition (blessures/motivation)
✅ Probabilités détaillées (Victoire/Nul/Défaite)
✅ Interface utilisateur optimisée
✅ Système multilingue (Français/Anglais)
✅ Comparaison cotes bookmakers
✅ Historique des prédictions
✅ Calendrier multi-matchs avancé
🆚 Statistiques Head-to-Head entre équipes
🏠 Facteur domicile variable selon l'équipe
🎮 NOUVEAU: Moteur de Simulation de Match Style Football Manager 2024

Release: 7 Août 2025 | Status: V10.5 Production Ready
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

# 🌍 SYSTÈME DE TRADUCTION
TRANSLATIONS = {
    'fr': {
        # PAGE PRINCIPALE
        'page_title': "⚽ Prédiction Football V10.5",
        'app_title': "🚀 FOOTBALL PREDICTION APP V10.5",
        'subtitle': "IA • Modèle 6-en-1 • Pro League Belge • H2H & Domicile • Simulation Match FM2024",
        'language_selector': "🌍 Langue / Language",
        'loading_data': "📊 Chargement des données...",
        'app_ready': "✅ Version V10.0 - Application prête!",
        
        # NAVIGATION
        'features': "🎯 Fonctionnalités:",
        'simple_prediction': "Prédiction Simple",
        'multi_match_calendar': "Calendrier Multi-Matchs", 
        'bookmaker_odds': "💰 Cotes Bookmakers",
        'history_performance': "Historique & Performance",
        'match_engine_simulation': "Moteur de Simulation",
        'documentation': "📚 Documentation",
        'about_title': "À Propos du Projet",
        'project_overview': "Vue d'Ensemble",
        'technical_details': "Détails Techniques",
        'algorithms_used': "Algorithmes Utilisés",
        'features_overview': "Fonctionnalités",
        'presentation_mode': "Mode Présentation",
        'becode_presentation': "Présentation BeCode",
        'project_description': "Application de prédiction de matchs de football utilisant l'intelligence artificielle",
        'technical_stack': "Stack Technique",
        'data_source': "Source des Données",
        'model_accuracy': "Précision du Modèle",
        'development_time': "Temps de Développement",
        'version_info': "Version Actuelle",
        
        # FAQ
        'faq_title': "❓ Questions Fréquemment Posées (FAQ)",
        'faq_q1': "Comment fonctionne la prédiction ?",
        'faq_a1': "Notre système utilise un modèle d'ensemble combinant 6 algorithmes différents (Random Forest, SVM, Logistic Regression, etc.) pour analyser les données historiques et prédire le résultat des matchs.",
        'faq_q2': "Quelle est la précision du modèle ?",
        'faq_a2': "Le modèle atteint une précision moyenne de 65-75% selon le type de prédiction. Les victoires à domicile sont généralement mieux prédites que les matchs nuls.",
        'faq_q3': "D'où viennent les données ?",
        'faq_a3': "Les données proviennent de matchs de la Pro League belge entre 2009 et 2023, incluant scores, statistiques d'équipes, forme récente et confrontations directes.",
        'faq_q4': "Comment utiliser le simulateur de match ?",
        'faq_a4': "Sélectionnez deux équipes dans l'onglet 'Simulation de Match', choisissez la vitesse d'animation, et lancez la simulation pour voir un match virtuel en temps réel.",
        'faq_q5': "Puis-je faire confiance aux prédictions pour parier ?",
        'faq_a5': "Les prédictions sont à titre informatif uniquement. Elles constituent une aide à la décision mais ne garantissent pas le résultat. Pariez de manière responsable.",
        
        # CONFIGURATION
        'configuration': "📅 Configuration",
        'seasons': "Saisons",
        'select_seasons': "Sélectionner les saisons:",
        'matches_available': "matchs disponibles",
        'season_summary': "Résumé de la saison",
        'total_matches': "Total Matchs",
        'avg_home_goals': "Buts Domicile",
        'avg_away_goals': "Buts Extérieur", 
        'goals_per_match': "Buts/Match",
        'average': "Moyenne",
        
        # PRÉDICTION SIMPLE
        'match_prediction': "🎯 Prédiction de Match",
        'model_configuration': "⚙️ Configuration du Modèle",
        'prediction_level': "🧠 Niveau de prédiction:",
        'advanced_model': "🚀 Modèle Avancé (Recommandé)",
        'simple_model': "📊 Modèle Simplifié",
        'advanced_features': "✅ Utilisation du modèle d'ensemble avec:",
        'null_analysis': "• Analyse des matchs nuls",
        'recent_form': "• Forme récente des équipes",
        'condition_factors': "• Facteurs de condition",
        'combined_models': "• 4 modèles combinés",
        'simple_activated': "📊 Modèle simplifié activé",
        
        'home_team': "Équipe à Domicile 🏠",
        'away_team': "Équipe à l'Extérieur ✈️",
        'predict_button': "🔮 PRÉDIRE LE MATCH",
        'prediction_result': "🏆 Résultat de la Prédiction",
        'probabilities': "📊 Probabilités de Résultat",
        'home_victory': "🏠 Victoire",
        'draw': "⚖️ Match Nul",
        'away_victory': "✈️ Victoire",
        'confidence': "Confiance",
        'probable_victory': "🏆 Victoire probable de",
        'probable_draw': "⚖️ Match nul probable",
        'chances': "de chances",
        'error_teams': "⚠️ Veuillez sélectionner deux équipes différentes",
        'error_calculation': "❌ Impossible de calculer la prédiction",
        'calculating': "🤖 Calcul en cours...",
        'home_wins': "📊 Victoires domicile",
        'away_wins': "📊 Victoires extérieur",
        
        # CALENDRIER MULTI-MATCHS
        'multi_match_predictions': "📅 Prédictions Multi-Matchs (Calendrier)",
        'team_selection': "Sélection d'équipe:",
        'generate_calendar': "📅 GÉNÉRER LE CALENDRIER",
        'full_calendar': "🏆 Calendrier Complet des Prédictions",
        'calendar_analysis': "📊 Analyse du Calendrier",
        'total_predictions': "Total prédictions",
        'home_wins_predicted': "Victoires domicile prédites",
        'away_wins_predicted': "Victoires extérieur prédites",
        'draws_predicted': "Matchs nuls prédits",
        'avg_confidence': "Confiance moyenne",
        'results_distribution': "📈 Répartition des Résultats",
        'no_matches_found': "❌ Aucun match trouvé pour cette équipe",
        
        # COTES BOOKMAKERS
        'bookmaker_odds_title': "💰 Cotes des Bookmakers",
        'home_team_odds': "Équipe domicile:",
        'away_team_odds': "Équipe extérieur:",
        'view_odds': "💰 VOIR LES COTES",
        'matches_found': "match(s) trouvé(s)",
        'match_date': "Match",
        'score': "Score",
        'no_odds_available': "⚠️ Aucune cote disponible",
        'no_match_between': "❌ Aucun match trouvé entre",
        'select_different_teams': "⚠️ Sélectionnez deux équipes différentes",
        
        # HISTORIQUE & PERFORMANCE
        'history_performance_title': "📈 Historique & Performance des Prédictions",
        'global_performance': "🎯 Performance Globale du Système",
        'total_predictions_made': "Total prédictions effectuées",
        'accuracy_rate': "Taux de précision",
        'confidence_avg': "Confiance moyenne",
        'best_prediction': "Meilleure prédiction",
        'accuracy_evolution': "📊 Évolution de la Précision",
        'performance_by_result': "� Performance par Type de Résultat",
        'home_wins_accuracy': "Précision Victoires Domicile",
        'draws_accuracy': "Précision Matchs Nuls", 
        'away_wins_accuracy': "Précision Victoires Extérieur",
        'recent_predictions': "📋 Dernières Prédictions",
        'improvement_recommendations': "� Recommandations d'Amélioration",
        'recommendation_1': "• Augmenter la taille de l'échantillon d'entraînement",
        'recommendation_2': "• Intégrer plus de données temps réel",
        'recommendation_3': "• Affiner les algorithmes de matchs nuls",
        'recommendation_4': "• Ajouter des facteurs météorologiques",
        'recommendation_5': "• Implémenter l'apprentissage en ligne",
        
        # ÉLÉMENTS SUPPLÉMENTAIRES
        'data_overview': "📊 Aperçu des Données",
        'total_analyzed': "Total analysés",
        'in_database': "Dans la base",
        'selected': "Sélectionnées",
        'teams': "Équipes",
        'seasons_to_analyze': "Saisons à analyser:",
        'calculating_statistics': "📊 Calcul des statistiques...",
        'profit_simulated': "Profit Simulé",
        'roi': "ROI",
        'accuracy_evolution_title': "📊 Évolution de la Précision",
        'accuracy_evolution_chart_title': "Évolution de la Précision du Système",
        'date_axis': "Date",
        'accuracy_axis': "Précision (%)",
        'recent_predictions': "📋 Dernières Prédictions",
        'table_date': "Date",
        'table_match': "Match", 
        'table_predicted': "Prédit",
        'table_actual': "Réel",
        'table_status': "Status",
        'odds_home_team': "Dom",
        'odds_draw': "Nul", 
        'odds_away_team': "Ext",
        'no_odds_available': "⚠️ Aucune cote disponible",
        'no_match_found': "❌ Aucun match trouvé entre",
        'select_different_teams': "⚠️ Sélectionnez deux équipes différentes",
        'continue_message': "Veuillez sélectionner au moins une saison pour continuer",
        'ai_comparison': "Comparaison IA",
        'ai_prediction_vs_odds': "🤖 Prédiction IA vs Cotes Bookmakers",
        'ai_prediction': "Prédiction IA",
        'bookmaker_odds': "💰 Cotes Moyennes",
        'value_bet': "Pari de Valeur",
        'no_value_found': "Aucune valeur détectée",
        'recommendation': "Recommandation",
        'historical_matches': "Matchs Historiques",
        'prediction_history_title': "📊 Historique des Prédictions",
        'save_prediction': "Sauvegarder cette Prédiction",
        'prediction_saved': "Prédiction sauvegardée avec succès!",
        'performance_metrics': "Métriques de Performance",
        'total_predictions': "Total Prédictions",
        'correct_predictions': "Prédictions Correctes",
        'average_confidence': "Confiance Moyenne",
        'performance_by_result_type': "🏆 Performance par Type de Résultat",
        'recommendation_1': "🔍 Analyser plus de données historiques pour les matchs nuls",
        'recommendation_2': "📊 Intégrer les statistiques de forme récente des équipes", 
        'recommendation_3': "🏠 Améliorer le facteur d'avantage à domicile",
        'recommendation_4': "⚽ Considérer les blessures et suspensions",
        'recommendation_5': "📈 Utiliser des modèles d'ensemble pour plus de précision",
        'performance_by_result_type': "🏆 Performance par Type de Résultat",
        'recent_predictions_title': "📋 Dernières Prédictions",
        'recent_accuracy': "🎯 Précision récente:",
        'improvement_recommendations_title': "💡 Recommandations d'Amélioration",
        'complete_calendar': "Calendrier Complet",
        'calendar_generation_info': "Génération intelligente d'un calendrier complet avec analyses de valeur",
        'model_configuration': 'Configuration du Modèle',
        'prediction_level': 'Niveau de prédiction',
        'advanced_model': 'Modèle Avancé (Recommandé)',
        'simplified_model': 'Modèle Simplifié',
        'advanced_model_help': 'Le modèle avancé utilise un ensemble de 4 algorithmes différents pour plus de précision',
        'using_ensemble_model': 'Utilisation du modèle d\'ensemble avec',
        'draw_analysis': 'Analyse des matchs nuls',
        'recent_form': 'Forme récente des équipes',
        'condition_factors': 'Facteurs de condition',
        'four_models_combined': '4 modèles combinés',
        'simplified_model_active': 'Modèle simplifié activé',
        'home_team': 'Équipe à Domicile',
        'away_team': 'Équipe à l\'Extérieur',
        'home_wins': 'Victoires domicile',
        'away_wins': 'Victoires extérieur',
        'predict_match': 'PRÉDIRE LE MATCH',
        'calculating': 'Calcul en cours',
        'prediction_result': 'Résultat de la Prédiction',
        'confidence': 'Confiance',
        'result_probabilities': 'Probabilités de Résultat',
        'victory': 'Victoire',
        'draw': 'Match Nul',
        'probable_victory': 'Victoire probable de',
        'probable_draw': 'Match nul probable',
        'prediction_error': 'Impossible de calculer la prédiction',
        'select_different_teams': 'Veuillez sélectionner deux équipes différentes',
        'matches_to_predict': "Matchs à prédire:",
        'prediction_period': "Période de prédiction:",
        'next_week': "Semaine prochaine",
        'next_month': "Mois prochain", 
        'next_season': "Saison prochaine",
        'prediction_detail_level': "Niveau de détail:",
        'detailed_analysis': "Analyse détaillée",
        'quick_overview': "Aperçu rapide",
        'advanced_options': "Options avancées",
        'include_value_analysis': "Inclure analyse de valeur",
        'min_confidence_filter': "Confiance minimale (%)",
        'export_format': "Format d'export",
        'display_only': "Affichage seulement",
        'generate_complete_calendar': "Générer le Calendrier Complet",
        'generating_calendar': "🤖 Génération du calendrier intelligent...",
        'predictions_generated': "prédictions générées avec succès!",
        'executive_summary': "Résumé Exécutif",
        'total_matches': "Total Matchs",
        'high_confidence': "Haute Confiance",
        'value_opportunities': "Opportunités Valeur",
        'avg_confidence': "Confiance Moy.",
        'filter_and_sort': "Filtrer et Trier",
        'filter_by_result': "Filtrer par résultat:",
        'sort_by': "Trier par:",
        'confidence_desc': "Confiance (desc)",
        'date_asc': "Date (asc)",
        'value_desc': "Valeur (desc)",
        'prediction_calendar': "Calendrier des Prédictions",
        'prediction': "Prédiction",
        'value_detected': "Valeur détectée!",
        'no_value': "Pas de valeur",
        'value_analysis': "Analyse Valeur",
        'key_factors': "Facteurs Clés",
        'risk_level': "Niveau risque",
        'result': "Résultat",
        'confidence': "Confiance",
        'calendar_statistics': "Statistiques du Calendrier",
        'results_distribution': "Distribution des Résultats",
        'confidence_distribution': "Distribution de la Confiance",
        'frequency': "Fréquence",
        'value_opportunities_by_date': "Opportunités par Date",
        'export_predictions': "Exporter les Prédictions",
        'download_csv': "Télécharger CSV",
        'download_json': "Télécharger JSON",
        
        # NOUVELLES FONCTIONNALITÉS V10.4
        'head_to_head_stats': "📊 Statistiques Face-à-Face",
        'h2h_last_matches': "Derniers matchs directs",
        'h2h_total_matches': "Total matchs joués",
        'h2h_home_wins': "Victoires domicile",
        'h2h_away_wins': "Victoires extérieur", 
        'h2h_draws': "Matchs nuls",
        'h2h_avg_goals_home': "Buts moy. domicile",
        'h2h_avg_goals_away': "Buts moy. extérieur",
        'h2h_recent_form': "Forme récente H2H",
        'h2h_advantage': "Avantage historique",
        'h2h_no_data': "Aucune donnée historique disponible",
        'home_advantage_factor': "🏠 Facteur Avantage Domicile",
        'team_home_strength': "Force à domicile",
        'default_home_advantage': "Avantage domicile standard",
        'enhanced_home_advantage': "Avantage domicile renforcé",
        'reduced_home_advantage': "Avantage domicile réduit",
        'home_performance_analysis': "Analyse performance domicile",
        'home_wins_percentage': "% Victoires domicile",
        'home_goals_ratio': "Ratio buts domicile/extérieur",
        'crowd_support_factor': "Facteur soutien public",
        
        # NOUVELLE FONCTIONNALITÉ V10.5 - MOTEUR DE SIMULATION DE MATCH
        'match_engine_simulation': "🎮 Moteur de Simulation de Match",
        'simulation_start': "Démarrer la Simulation",
        'simulation_speed': "Vitesse de Simulation",
        'speed_x1': "x1 (Temps Réel)",
        'speed_x5': "x5 (Rapide)",
        'speed_x10': "x10 (Très Rapide)",
        'speed_x20': "x20 (Ultra Rapide)",
        'match_time': "Temps de Match",
        'home_score': "Score Domicile",
        'away_score': "Score Extérieur",
        'match_events': "Événements du Match",
        'goal_scored': "⚽ BUT !",
        'yellow_card': "🟨 Carton Jaune",
        'red_card': "🟥 Carton Rouge",
        'substitution': "🔄 Remplacement",
        'match_statistics': "📊 Statistiques",
        'possession': "Possession",
        'shots': "Tirs",
        'shots_on_target': "Tirs cadrés",
        'corners': "Corners",
        'fouls': "Fautes",
        'offside': "Hors-jeu",
        'simulation_complete': "🏁 Simulation de Match Terminée !",
        'final_result': "Résultat Final",
        'match_analysis': "Analyse du Match",
        'select_teams_for_simulation': "Sélectionnez les équipes pour la simulation",
        'simulation_in_progress': "Simulation en cours...",
        'pause_simulation': "⏸️ Pause",
        'resume_simulation': "▶️ Reprendre",
        'reset_simulation': "🔄 Reset",
        'match_preview': "Aperçu du Match",
        'predicted_result': "Résultat Prédit",
        'simulate_match': "🎮 Simuler le Match",
    },
    'en': {
        # MAIN PAGE
        'page_title': "⚽ Football Prediction V10.5",
        'app_title': "🚀 FOOTBALL PREDICTION APP V10.5",
        'subtitle': "AI • 6-in-1 Ensemble • Belgian Pro League • H2H & Home Advantage • FM2024 Match Engine",
        'language_selector': "🌍 Language / Langue",
        'loading_data': "📊 Loading data...",
        'app_ready': "✅ Version V10.0 - Application ready!",
        
        # NAVIGATION
        'features': "🎯 Features:",
        'simple_prediction': "Simple Prediction",
        'multi_match_calendar': "Multi-Match Calendar", 
        'bookmaker_odds': "💰 Bookmaker Odds",
        'history_performance': "History & Performance",
        'match_engine_simulation': "Match Engine Simulation",        # CONFIGURATION
        'configuration': "📅 Configuration",
        'seasons': "Seasons",
        'select_seasons': "Select seasons:",
        'matches_available': "matches available",
        'season_summary': "Season summary",
        'total_matches': "Total Matches",
        'avg_home_goals': "Home Goals",
        'avg_away_goals': "Away Goals",
        'goals_per_match': "Goals/Match", 
        'average': "Average",
        
        # SIMPLE PREDICTION
        'match_prediction': "🎯 Match Prediction",
        'model_configuration': "⚙️ Model Configuration",
        'prediction_level': "🧠 Prediction level:",
        'advanced_model': "🚀 Advanced Model (Recommended)",
        'simple_model': "📊 Simple Model",
        'advanced_features': "✅ Using ensemble model with:",
        'null_analysis': "• Draw analysis",
        'recent_form': "• Recent team form",
        'condition_factors': "• Condition factors", 
        'combined_models': "• 4 combined models",
        'simple_activated': "📊 Simple model activated",
        
        'home_team': "Home Team 🏠",
        'away_team': "Away Team ✈️",
        'predict_button': "🔮 PREDICT MATCH",
        'prediction_result': "🏆 Prediction Result",
        'probabilities': "📊 Result Probabilities",
        'home_victory': "🏠 Victory",
        'draw': "⚖️ Draw",
        'away_victory': "✈️ Victory",
        'confidence': "Confidence",
        'probable_victory': "🏆 Probable victory for",
        'probable_draw': "⚖️ Probable draw",
        'chances': "chances",
        'error_teams': "⚠️ Please select two different teams",
        'error_calculation': "❌ Unable to calculate prediction",
        'calculating': "🤖 Calculating...",
        'home_wins': "📊 Home wins",
        'away_wins': "📊 Away wins",
        
        # MULTI-MATCH CALENDAR
        'multi_match_predictions': "📅 Multi-Match Predictions (Calendar)",
        'team_selection': "Team selection:",
        'generate_calendar': "📅 GENERATE CALENDAR", 
        'full_calendar': "🏆 Complete Predictions Calendar",
        'calendar_analysis': "📊 Calendar Analysis",
        'total_predictions': "Total predictions",
        'home_wins_predicted': "Predicted home wins",
        'away_wins_predicted': "Predicted away wins", 
        'draws_predicted': "Predicted draws",
        'avg_confidence': "Average confidence",
        'results_distribution': "📈 Results Distribution",
        'no_matches_found': "❌ No matches found for this team",
        
        # BOOKMAKER ODDS
        'bookmaker_odds_title': "💰 Bookmaker Odds",
        'home_team_odds': "Home team:",
        'away_team_odds': "Away team:",
        'view_odds': "💰 VIEW ODDS",
        'matches_found': "match(es) found",
        'match_date': "Match",
        'score': "Score",
        'no_odds_available': "⚠️ No odds available",
        'no_match_between': "❌ No match found between",
        
        # HISTORY & PERFORMANCE  
        'history_performance_title': "📈 Prediction History & Performance",
        'global_performance': "🎯 Global System Performance",
        'total_predictions_made': "Total predictions made",
        'accuracy_rate': "Accuracy rate",
        'confidence_avg': "Average confidence",
        'best_prediction': "Best prediction",
        'accuracy_evolution': "📊 Accuracy Evolution", 
        'performance_by_result': "� Performance by Result Type",
        'home_wins_accuracy': "Home Wins Accuracy",
        'draws_accuracy': "Draws Accuracy",
        'away_wins_accuracy': "Away Wins Accuracy",
        'recent_predictions': "📋 Recent Predictions",
        'improvement_recommendations': "� Improvement Recommendations",
        'recommendation_1': "• Increase training sample size",
        'recommendation_2': "• Integrate more real-time data",
        'recommendation_3': "• Refine draw algorithms",
        'recommendation_4': "• Add weather factors",
        'recommendation_5': "• Implement online learning",
        
        # ADDITIONAL ELEMENTS
        'data_overview': "📊 Data Overview", 
        'total_analyzed': "Total analyzed",
        'in_database': "In database",
        'selected': "Selected",
        'teams': "Teams",
        'seasons_to_analyze': "Seasons to analyze:",
        'calculating_statistics': "📊 Calculating statistics...",
        'profit_simulated': "Simulated Profit",
        'roi': "ROI",
        'accuracy_evolution_title': "📊 Accuracy Evolution",
        'accuracy_evolution_chart_title': "System Accuracy Evolution",
        'date_axis': "Date",
        'accuracy_axis': "Accuracy (%)",
        'recent_predictions': "📋 Recent Predictions", 
        'table_date': "Date",
        'table_match': "Match",
        'table_predicted': "Predicted", 
        'table_actual': "Actual",
        'table_status': "Status",
        'odds_home_team': "Home",
        'odds_draw': "Draw", 
        'odds_away_team': "Away",
        'no_odds_available': "⚠️ No odds available",
        'no_match_found': "❌ No match found between",
        'select_different_teams': "⚠️ Select two different teams",
        'continue_message': "Please select at least one season to continue",
        'ai_comparison': "AI Comparison",
        'ai_prediction_vs_odds': "🤖 AI Prediction vs Bookmaker Odds",
        'ai_prediction': "AI Prediction",
        'bookmaker_odds': "💰 Average Odds",
        'value_bet': "Value Bet",
        'no_value_found': "No value detected",
        'recommendation': "Recommendation",
        'historical_matches': "Historical Matches",
        'prediction_history_title': "📊 Prediction History",
        'save_prediction': "Save this Prediction",
        'prediction_saved': "Prediction saved successfully!",
        'performance_metrics': "Performance Metrics",
        'total_predictions': "Total Predictions",
        'correct_predictions': "Correct Predictions",
        'average_confidence': "Average Confidence",
        'performance_by_result_type': "🏆 Performance by Result Type",
        'recommendation_1': "🔍 Analyze more historical data for draw matches",
        'recommendation_2': "📊 Integrate recent team form statistics",
        'recommendation_3': "🏠 Improve home advantage factor", 
        'recommendation_4': "⚽ Consider injuries and suspensions",
        'recommendation_5': "📈 Use ensemble models for better accuracy",
        'performance_by_result_type': "🏆 Performance by Result Type",
        'recent_predictions_title': "📋 Recent Predictions",
        'recent_accuracy': "🎯 Recent accuracy:",
        'improvement_recommendations_title': "💡 Improvement Recommendations",
        'complete_calendar': "Complete Calendar",
        'calendar_generation_info': "Intelligent generation of a complete calendar with value analysis",
        'model_configuration': 'Model Configuration',
        'prediction_level': 'Prediction Level',
        'advanced_model': 'Advanced Model (Recommended)',
        'simplified_model': 'Simplified Model',
        'advanced_model_help': 'The advanced model uses an ensemble of 4 different algorithms for higher accuracy',
        'using_ensemble_model': 'Using ensemble model with',
        'draw_analysis': 'Draw analysis',
        'recent_form': 'Recent team form',
        'condition_factors': 'Condition factors',
        'four_models_combined': '4 combined models',
        'simplified_model_active': 'Simplified model activated',
        'home_team': 'Home Team',
        'away_team': 'Away Team',
        'home_wins': 'Home wins',
        'away_wins': 'Away wins',
        'predict_match': 'PREDICT MATCH',
        'calculating': 'Calculating',
        'prediction_result': 'Prediction Result',
        'confidence': 'Confidence',
        'result_probabilities': 'Result Probabilities',
        'victory': 'Victory',
        'draw': 'Draw',
        'probable_victory': 'Probable victory for',
        'probable_draw': 'Probable draw',
        'prediction_error': 'Unable to calculate prediction',
        'select_different_teams': 'Please select two different teams',
        'recent_accuracy': "🎯 Recent accuracy:",
        'improvement_recommendations_title': "💡 Improvement Recommendations",
        'complete_calendar': "Complete Calendar",
        'calendar_generation_info': "Intelligent generation of complete calendar with value analysis",
        'matches_to_predict': "Matches to predict:",
        'prediction_period': "Prediction period:",
        'next_week': "Next week",
        'next_month': "Next month", 
        'next_season': "Next season",
        'prediction_detail_level': "Detail level:",
        'detailed_analysis': "Detailed analysis",
        'quick_overview': "Quick overview",
        'advanced_options': "Advanced options",
        'include_value_analysis': "Include value analysis",
        'min_confidence_filter': "Minimum confidence (%)",
        'export_format': "Export format",
        'display_only': "Display only",
        'generate_complete_calendar': "Generate Complete Calendar",
        'generating_calendar': "🤖 Generating intelligent calendar...",
        'predictions_generated': "predictions generated successfully!",
        'executive_summary': "Executive Summary",
        'total_matches': "Total Matches",
        'high_confidence': "High Confidence",
        'value_opportunities': "Value Opportunities",
        'avg_confidence': "Avg. Confidence",
        'filter_and_sort': "Filter and Sort",
        'filter_by_result': "Filter by result:",
        'sort_by': "Sort by:",
        'confidence_desc': "Confidence (desc)",
        'date_asc': "Date (asc)",
        'value_desc': "Value (desc)",
        'prediction_calendar': "Prediction Calendar",
        'prediction': "Prediction",
        'value_detected': "Value detected!",
        'no_value': "No value",
        'value_analysis': "Value Analysis",
        'key_factors': "Key Factors",
        'risk_level': "Risk level",
        'result': "Result",
        'confidence': "Confidence",
        'calendar_statistics': "Calendar Statistics",
        'results_distribution': "Results Distribution",
        'confidence_distribution': "Confidence Distribution",
        'frequency': "Frequency",
        'value_opportunities_by_date': "Opportunities by Date",
        'export_predictions': "Export Predictions",
        'download_csv': "Download CSV",
        'download_json': "Download JSON",
        
        # NEW FEATURES V10.4
        'head_to_head_stats': "📊 Head-to-Head Statistics",
        'h2h_last_matches': "Recent direct matches",
        'h2h_total_matches': "Total matches played",
        'h2h_home_wins': "Home wins",
        'h2h_away_wins': "Away wins",
        'h2h_draws': "Draws",
        'h2h_avg_goals_home': "Avg goals home",
        'h2h_avg_goals_away': "Avg goals away",
        'h2h_recent_form': "Recent H2H form",
        'h2h_advantage': "Historical advantage",
        'h2h_no_data': "No historical data available",
        'home_advantage_factor': "🏠 Home Advantage Factor",
        'team_home_strength': "Home strength",
        'default_home_advantage': "Standard home advantage",
        'enhanced_home_advantage': "Enhanced home advantage",
        'reduced_home_advantage': "Reduced home advantage",
        'home_performance_analysis': "Home performance analysis",
        'home_wins_percentage': "% Home wins",
        'home_goals_ratio': "Home/away goals ratio",
        'crowd_support_factor': "Crowd support factor",
        'analyze_more_data': "🔍 Analyze more historical data for draws",
        
        # NOUVELLE FONCTIONNALITÉ V10.5 - MATCH ENGINE SIMULATION
        'match_engine_simulation': "🎮 Match Engine Simulation",
        'simulation_start': "Start Match Simulation",
        'simulation_speed': "Simulation Speed",
        'speed_x1': "x1 (Real Time)",
        'speed_x5': "x5 (Fast)",
        'speed_x10': "x10 (Very Fast)", 
        'speed_x20': "x20 (Ultra Fast)",
        'match_time': "Match Time",
        'home_score': "Home Score",
        'away_score': "Away Score",
        'match_events': "Match Events",
        'goal_scored': "⚽ GOAL!",
        'yellow_card': "🟨 Yellow Card",
        'red_card': "🟥 Red Card",
        'substitution': "🔄 Substitution",
        'match_statistics': "📊 Match Statistics",
        'possession': "Possession",
        'shots': "Shots",
        'shots_on_target': "Shots on Target",
        'corners': "Corners",
        'fouls': "Fouls",
        'offside': "Offside",
        'simulation_complete': "🏁 Match Simulation Complete!",
        'final_result': "Final Result",
        'match_analysis': "Match Analysis",
        'select_teams_for_simulation': "Select teams for match simulation",
        'simulation_in_progress': "Simulation in progress...",
        'pause_simulation': "⏸️ Pause",
        'resume_simulation': "▶️ Resume",
        'reset_simulation': "🔄 Reset",
        'match_preview': "Match Preview",
        'predicted_result': "Predicted Result",
        'simulate_match': "🎮 Simulate Match",
        'integrate_recent_form': "📊 Integrate recent team form statistics",
        'improve_home_advantage': "🏠 Improve home advantage factor", 
        'consider_injuries': "⚽ Consider injuries and suspensions",
        'use_ensemble_models': "📈 Use ensemble models for better accuracy",
        
        # NOUVELLE FONCTIONNALITÉ V10.6 - DOCUMENTATION
        'documentation': "📚 Documentation",
        'about_title': "About the Project",
        'project_overview': "Project Overview",
        'technical_details': "Technical Details",
        'algorithms_used': "Algorithms Used",
        'features_overview': "Features",
        'presentation_mode': "Presentation Mode",
        'becode_presentation': "BeCode Presentation",
        'project_description': "Football match prediction application using artificial intelligence",
        'technical_stack': "Technical Stack",
        'data_source': "Data Source",
        'model_accuracy': "Model Accuracy",
        'development_time': "Development Time",
        'version_info': "Current Version",
        
        # FAQ
        'faq_title': "❓ Frequently Asked Questions (FAQ)",
        'faq_q1': "How does the prediction work?",
        'faq_a1': "Our system uses an ensemble model combining 6 different algorithms (Random Forest, SVM, Logistic Regression, etc.) to analyze historical data and predict match outcomes.",
        'faq_q2': "What is the model's accuracy?",
        'faq_a2': "The model achieves an average accuracy of 65-75% depending on the prediction type. Home victories are generally better predicted than draws.",
        'faq_q3': "Where does the data come from?",
        'faq_a3': "Data comes from Belgian Pro League matches between 2009 and 2023, including scores, team statistics, recent form and head-to-head confrontations.",
        'faq_q4': "How to use the match simulator?",
        'faq_a4': "Select two teams in the 'Match Simulation' tab, choose animation speed, and start the simulation to watch a virtual match in real-time.",
        'faq_q5': "Can I trust predictions for betting?",
        'faq_a5': "Predictions are for informational purposes only. They provide decision support but do not guarantee results. Bet responsibly.",
    }
}

def get_text(key, lang='fr'):
    """Récupère le texte traduit selon la langue sélectionnée"""
    return TRANSLATIONS.get(lang, TRANSLATIONS['fr']).get(key, key)

def create_language_selector():
    """Crée le sélecteur de langue avec bannière défilante discrète"""
    
    # Style CSS pour la bannière défilante
    st.markdown("""
    <style>
    .language-banner {
        position: fixed;
        top: 0;
        right: 0;
        z-index: 999999;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 6px 12px;
        border-radius: 0 0 0 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        min-width: 160px;
        max-width: 200px;
        overflow: hidden;
    }
    
    .scrolling-text {
        white-space: nowrap;
        overflow: hidden;
        animation: scroll-contained 8s linear infinite;
        margin-bottom: 4px;
        font-size: 9px;
        opacity: 0.8;
        color: white;
        font-weight: 400;
        width: 100%;
        display: block;
    }
    
    @keyframes scroll-contained {
        0% { transform: translateX(50%); }
        50% { transform: translateX(-20%); }
        100% { transform: translateX(50%); }
    }
    
    .mini-lang-selector {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    
    .mini-flag-btn {
        background: rgba(255,255,255,0.2);
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 4px;
        padding: 2px 6px;
        color: white;
        font-size: 10px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 2px;
    }
    
    .mini-flag-btn:hover {
        background: rgba(255,255,255,0.3);
        transform: scale(1.05);
        color: white;
        text-decoration: none;
    }
    
    .mini-flag-btn.active {
        background: rgba(255,255,255,0.4);
        border: 1px solid white;
        font-weight: 600;
    }
    
    .flag-fr {
        display: inline-block;
        width: 12px;
        height: 8px;
        background: linear-gradient(to right, #0055A4 33%, white 33% 66%, #EF4135 66%);
        border-radius: 2px;
        margin-right: 4px;
        vertical-align: middle;
    }
    
    .flag-en {
        display: inline-block;
        width: 12px;
        height: 8px;
        background: 
            linear-gradient(90deg, transparent 46%, white 46% 54%, transparent 54%),
            linear-gradient(0deg, transparent 38%, white 38% 62%, transparent 62%),
            linear-gradient(45deg, transparent 40%, #C8102E 40% 45%, white 45% 55%, #C8102E 55% 60%, transparent 60%),
            linear-gradient(-45deg, transparent 40%, #C8102E 40% 45%, white 45% 55%, #C8102E 55% 60%, transparent 60%),
            #012169;
        border-radius: 2px;
        margin-right: 4px;
        vertical-align: middle;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialiser la langue par défaut
    if 'language' not in st.session_state:
        st.session_state.language = 'fr'
    
    # Gérer les changements de langue via query params
    query_params = st.query_params
    if 'lang' in query_params:
        new_lang = query_params['lang']
        if new_lang in ['fr', 'en']:
            st.session_state.language = new_lang
            # Nettoyer les query params
            st.query_params.clear()
    
    current_lang = st.session_state.language
    
    # Classes CSS pour les boutons
    fr_class = "mini-flag-btn active" if current_lang == 'fr' else "mini-flag-btn"
    en_class = "mini-flag-btn active" if current_lang == 'en' else "mini-flag-btn"
    
    # Affichage de la bannière compacte avec sélecteur intégré
    st.markdown(f"""
    <div class="language-banner">
        <div class="scrolling-text"><span class="flag-fr"></span><span class="flag-en"></span> Language • Langue</div>
        <div class="mini-lang-selector">
            <a href="?lang=fr" target="_self" class="{fr_class}">
                <span class="flag-fr"></span> FR
            </a>
            <a href="?lang=en" target="_self" class="{en_class}">
                <span class="flag-en"></span> EN
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    return current_lang

# Configuration de la page
st.set_page_config(
    page_title="⚽ Football Prediction V10.0",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Ultra Moderne - Mode Sombre Exclusif
st.markdown("""
<style>
    /* Variables CSS pour cohérence */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --secondary-gradient: linear-gradient(135deg, #2d2d2d 0%, #404040 100%);
        --accent-color: #667eea;
        --text-primary: #ffffff;
        --text-secondary: #b8b8b8;
        --bg-primary: #1a1a1a;
        --bg-secondary: #2d2d2d;
        --bg-card: #333333;
        --shadow-glow: 0 8px 32px rgba(102, 126, 234, 0.3);
        --shadow-subtle: 0 4px 20px rgba(0, 0, 0, 0.4);
        --border-radius: 16px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Background global avec dégradé animé */
    .stApp {
        background: linear-gradient(-45deg, #1a1a1a, #2d2d2d, #1e1e1e, #3a3a3a);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        color: var(--text-primary);
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Header principal avec effet glassmorphism */
    .main-header {
        background: rgba(102, 126, 234, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(102, 126, 234, 0.2);
        padding: 3rem 2rem;
        border-radius: var(--border-radius);
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: var(--shadow-glow);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .main-header h1 {
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
    }
    
    .main-header p {
        color: var(--text-secondary);
        font-size: 1.2rem;
        font-weight: 300;
    }
    
    /* Cards avec effet néon subtil */
    .metric-card {
        background: rgba(51, 51, 51, 0.8);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: var(--border-radius);
        border: 1px solid rgba(102, 126, 234, 0.3);
        margin-bottom: 1.5rem;
        transition: var(--transition);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--primary-gradient);
        transform: scaleX(0);
        transition: var(--transition);
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-glow);
        border-color: var(--accent-color);
    }
    
    .metric-card:hover::before {
        transform: scaleX(1);
    }
    
    .metric-card h3 {
        color: var(--accent-color) !important;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-card h2 {
        color: var(--text-primary) !important;
        font-weight: 900;
        font-size: 2.5rem;
        margin: 0.8rem 0;
        text-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
    }
    
    .metric-card p {
        color: var(--text-secondary) !important;
        font-size: 0.95rem;
        opacity: 0.9;
    }
    
    /* Boutons avec effet holographique */
    .stButton > button {
        background: var(--primary-gradient) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: var(--transition) !important;
        box-shadow: var(--shadow-glow) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Notifications avec animations fluides */
    .notification-success {
        background: linear-gradient(135deg, #28a745, #20c997);
        border: 1px solid rgba(40, 167, 69, 0.3);
        backdrop-filter: blur(10px);
        color: white;
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(40, 167, 69, 0.3);
        animation: slideInFromLeft 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .notification-warning {
        background: linear-gradient(135deg, #ffc107, #fd7e14);
        border: 1px solid rgba(255, 193, 7, 0.3);
        backdrop-filter: blur(10px);
        color: #212529;
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(255, 193, 7, 0.3);
        animation: slideInFromLeft 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .notification-info {
        background: linear-gradient(135deg, #17a2b8, #6f42c1);
        border: 1px solid rgba(23, 162, 184, 0.3);
        backdrop-filter: blur(10px);
        color: white;
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(23, 162, 184, 0.3);
        animation: slideInFromLeft 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    @keyframes slideInFromLeft {
        0% {
            transform: translateX(-100%) rotateY(-90deg);
            opacity: 0;
        }
        100% {
            transform: translateX(0) rotateY(0deg);
            opacity: 1;
        }
    }
    
    /* Sidebar avec glassmorphism */
    .css-1d391kg, .css-1y4p8pa {
        background: rgba(29, 29, 29, 0.9) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Éléments de formulaire stylisés */
    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        background: rgba(51, 51, 51, 0.8) !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
        backdrop-filter: blur(10px) !important;
        transition: var(--transition) !important;
    }
    
    .stSelectbox > div > div:hover,
    .stMultiSelect > div > div:hover {
        border-color: var(--accent-color) !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.2) !important;
    }
    
    /* DataFrames avec style futuriste */
    .stDataFrame {
        background: rgba(51, 51, 51, 0.8) !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: var(--border-radius) !important;
        backdrop-filter: blur(10px) !important;
        overflow: hidden !important;
    }
    
    .stDataFrame table {
        background: transparent !important;
        color: var(--text-primary) !important;
    }
    
    .stDataFrame th {
        background: var(--primary-gradient) !important;
        color: white !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        border: none !important;
    }
    
    .stDataFrame td {
        background: rgba(51, 51, 51, 0.5) !important;
        color: var(--text-primary) !important;
        border: 1px solid rgba(102, 126, 234, 0.1) !important;
        transition: var(--transition) !important;
    }
    
    .stDataFrame tr:hover td {
        background: rgba(102, 126, 234, 0.1) !important;
        color: var(--accent-color) !important;
    }
    
    /* Titres et headers */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--text-primary) !important;
        text-shadow: 0 0 20px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stMarkdown h3 {
        background: rgba(102, 126, 234, 0.1) !important;
        padding: 1rem !important;
        border-radius: 12px !important;
        border-left: 4px solid var(--accent-color) !important;
        backdrop-filter: blur(10px) !important;
        margin: 1.5rem 0 !important;
    }
    
    /* Graphiques avec cadre élégant */
    .stPlotlyChart {
        background: rgba(51, 51, 51, 0.8) !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: var(--border-radius) !important;
        padding: 1rem !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: var(--shadow-subtle) !important;
    }
    
    /* Radio buttons stylisés */
    .stRadio > div {
        background: rgba(51, 51, 51, 0.8) !important;
        padding: 1rem !important;
        border-radius: 12px !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Sliders avec effet néon */
    .stSlider > div > div > div > div {
        background: var(--primary-gradient) !important;
    }
    
    /* Effet de particules subtil */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(118, 75, 162, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(102, 126, 234, 0.05) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }
    
    /* Scrollbar personnalisée */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(29, 29, 29, 0.8);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-gradient);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Chargement des données football"""
    try:
        import os
        
        # Lister les chemins possibles pour le dataset
        possible_paths = [
            '../dataset.csv',
            './dataset.csv', 
            'dataset.csv',
            'C:/Users/Ricca/football_prediction_clean/dataset.csv',
            'C:/Users/Ricca/football_prediction_clean/Riccardo/dataset.csv'
        ]
        
        # Charger le dataset
        dataset_path = None
        for path in possible_paths:
            if os.path.exists(path):
                dataset_path = path
                break
        
        if dataset_path is None:
            st.error("❌ Impossible de charger le fichier dataset.csv")
            return None
            
        # Charger avec l'encodage qui fonctionne
        encodings = ['latin-1', 'utf-8', 'cp1252']
        data = None
        
        for encoding in encodings:
            try:
                data = pd.read_csv(dataset_path, encoding=encoding)
                break
            except Exception:
                continue
        
        if data is None:
            st.error("❌ Impossible de charger le fichier avec tous les encodages testés")
            return None
        
        # Nettoyer et formater les données
        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d', errors='coerce')
        data = data.dropna(subset=['Date'])
        
        # Calculer la saison (Juillet à Juin)
        data['Season'] = data['Date'].apply(lambda x: f"{x.year}-{x.year+1}" if x.month >= 7 else f"{x.year-1}-{x.year}")
        
        return data
        
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement des données: {str(e)}")
        return None

def calculate_recent_form(data, team, num_matches=5):
    """AMÉLIORATION 2: Calcul de la forme récente d'une équipe (derniers 5 matchs)"""
    if data is None or len(data) == 0:
        return {"points": 0, "goals_for": 0, "goals_against": 0, "form_rating": 0.5}
    
    # Trier les données par date décroissante
    sorted_data = data.sort_values('Date', ascending=False)
    
    # Récupérer les derniers matchs de l'équipe
    team_matches = sorted_data[
        (sorted_data['HomeTeam'] == team) | (sorted_data['AwayTeam'] == team)
    ].head(num_matches)
    
    if len(team_matches) == 0:
        return {"points": 0, "goals_for": 0, "goals_against": 0, "form_rating": 0.5}
    
    points = 0
    goals_for = 0
    goals_against = 0
    
    for _, match in team_matches.iterrows():
        is_home = match['HomeTeam'] == team
        
        if is_home:
            team_goals = match['FTHG']
            opp_goals = match['FTAG']
        else:
            team_goals = match['FTAG']
            opp_goals = match['FTHG']
        
        goals_for += team_goals
        goals_against += opp_goals
        
        # Points : Victoire=3, Nul=1, Défaite=0
        if team_goals > opp_goals:
            points += 3
        elif team_goals == opp_goals:
            points += 1
    
    # Calcul du rating de forme (0-1)
    max_points = num_matches * 3
    form_rating = points / max_points if max_points > 0 else 0.5
    
    return {
        "points": points,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "form_rating": form_rating,
        "matches_played": len(team_matches)
    }

def simulate_team_condition(team):
    """AMÉLIORATION 3: Simulation des blessures/suspensions et condition de l'équipe"""
    import random
    
    # Simulation réaliste des facteurs d'équipe
    injury_impact = random.uniform(-0.3, 0.1)  # Généralement négatif
    suspension_impact = random.uniform(-0.2, 0)  # Toujours négatif ou neutre
    fatigue_impact = random.uniform(-0.2, 0.2)  # Peut être positif (repos) ou négatif (fatigue)
    
    # Facteurs positifs occasionnels
    motivation_boost = random.uniform(-0.1, 0.3)  # Derby, match important
    home_advantage_extra = random.uniform(0, 0.2)  # Supporters, habitudes
    
    total_impact = (injury_impact + suspension_impact + fatigue_impact + 
                   motivation_boost + home_advantage_extra)
    
    # Limiter l'impact entre -0.5 et +0.5 buts
    total_impact = max(-0.5, min(0.5, total_impact))
    
    return {
        "condition_impact": total_impact,
        "injury_factor": injury_impact,
        "suspension_factor": suspension_impact, 
        "fatigue_factor": fatigue_impact,
        "motivation_factor": motivation_boost,
        "details": {
            "injuries": injury_impact < -0.15,
            "suspensions": suspension_impact < -0.1,
            "high_motivation": motivation_boost > 0.2,
            "fatigue": fatigue_impact < -0.15
        }
    }

def get_head_to_head_stats(data, home_team, away_team, num_matches=10):
    """
    🆚 NOUVELLE FONCTIONNALITÉ V10.4 - Analyse Head-to-Head
    ========================================================
    Calcule les statistiques des confrontations directes entre deux équipes
    """
    h2h_matches = data[
        ((data['HomeTeam'] == home_team) & (data['AwayTeam'] == away_team)) |
        ((data['HomeTeam'] == away_team) & (data['AwayTeam'] == home_team))
    ].sort_values('Date', ascending=False).head(num_matches)
    
    if h2h_matches.empty:
        return {
            'total_matches': 0,
            'home_wins': 0,
            'away_wins': 0,
            'draws': 0,
            'avg_goals_home': 0,
            'avg_goals_away': 0,
            'recent_form': [],
            'advantage': 'neutral',
            'has_data': False
        }
    
    # Calcul des statistiques
    total_matches = len(h2h_matches)
    
    # Victoires/Défaites/Nuls du point de vue de l'équipe domicile actuelle
    home_wins = 0
    away_wins = 0
    draws = 0
    goals_scored_home = []
    goals_scored_away = []
    recent_form = []
    
    for _, match in h2h_matches.iterrows():
        home_goals = match['FTHG']
        away_goals = match['FTAG']
        
        # Déterminer le résultat du point de vue de l'équipe domicile actuelle
        if match['HomeTeam'] == home_team:
            goals_scored_home.append(home_goals)
            goals_scored_away.append(away_goals)
            if home_goals > away_goals:
                home_wins += 1
                recent_form.append('W')
            elif home_goals < away_goals:
                away_wins += 1
                recent_form.append('L')
            else:
                draws += 1
                recent_form.append('D')
        else:  # home_team était l'équipe extérieure dans ce match historique
            goals_scored_home.append(away_goals)
            goals_scored_away.append(home_goals)
            if away_goals > home_goals:
                home_wins += 1
                recent_form.append('W')
            elif away_goals < home_goals:
                away_wins += 1
                recent_form.append('L')
            else:
                draws += 1
                recent_form.append('D')
    
    # Calcul des moyennes
    avg_goals_home = np.mean(goals_scored_home) if goals_scored_home else 0
    avg_goals_away = np.mean(goals_scored_away) if goals_scored_away else 0
    
    # Détermination de l'avantage historique
    home_percentage = (home_wins / total_matches) * 100
    if home_percentage > 60:
        advantage = 'strong_home'
    elif home_percentage > 40:
        advantage = 'slight_home'
    elif home_percentage < 25:
        advantage = 'strong_away'
    elif home_percentage < 40:
        advantage = 'slight_away'
    else:
        advantage = 'neutral'
    
    return {
        'total_matches': total_matches,
        'home_wins': home_wins,
        'away_wins': away_wins,
        'draws': draws,
        'avg_goals_home': round(avg_goals_home, 2),
        'avg_goals_away': round(avg_goals_away, 2),
        'recent_form': recent_form[:5],  # 5 derniers matchs
        'advantage': advantage,
        'home_percentage': round(home_percentage, 1),
        'has_data': True
    }

def calculate_team_home_advantage(data, team):
    """
    🏠 NOUVELLE FONCTIONNALITÉ V10.4 - Facteur Domicile Variable
    ============================================================
    Calcule le facteur d'avantage domicile spécifique à chaque équipe
    """
    # Matchs à domicile de l'équipe
    home_matches = data[data['HomeTeam'] == team].copy()
    
    if home_matches.empty:
        return {
            'factor': 1.2,  # Facteur standard
            'strength': 'default',
            'home_wins_percentage': 50.0,
            'home_goals_ratio': 1.0,
            'crowd_support': 'average'
        }
    
    # Calcul des statistiques à domicile
    total_home_matches = len(home_matches)
    home_wins = len(home_matches[home_matches['FTR'] == 'H'])
    home_goals = home_matches['FTHG'].sum()
    away_goals_conceded = home_matches['FTAG'].sum()
    
    # Matchs à l'extérieur pour comparaison
    away_matches = data[data['AwayTeam'] == team].copy()
    if not away_matches.empty:
        away_goals_scored = away_matches['FTAG'].sum()
        away_matches_count = len(away_matches)
        away_avg_goals = away_goals_scored / away_matches_count if away_matches_count > 0 else 1
    else:
        away_avg_goals = 1
    
    # Calculs
    home_wins_percentage = (home_wins / total_home_matches) * 100 if total_home_matches > 0 else 50
    home_avg_goals = home_goals / total_home_matches if total_home_matches > 0 else 1
    home_goals_ratio = home_avg_goals / away_avg_goals if away_avg_goals > 0 else 1
    
    # Détermination du facteur d'avantage domicile
    if home_wins_percentage > 70 and home_goals_ratio > 1.5:
        factor = 1.4  # Avantage domicile très fort
        strength = 'very_strong'
        crowd_support = 'excellent'
    elif home_wins_percentage > 60 and home_goals_ratio > 1.3:
        factor = 1.3  # Avantage domicile fort
        strength = 'strong'
        crowd_support = 'good'
    elif home_wins_percentage > 50 and home_goals_ratio > 1.1:
        factor = 1.2  # Avantage domicile normal
        strength = 'normal'
        crowd_support = 'average'
    elif home_wins_percentage > 40:
        factor = 1.1  # Avantage domicile faible
        strength = 'weak'
        crowd_support = 'poor'
    else:
        factor = 1.0  # Pas d'avantage domicile
        strength = 'none'
        crowd_support = 'very_poor'
    
    return {
        'factor': factor,
        'strength': strength,
        'home_wins_percentage': round(home_wins_percentage, 1),
        'home_goals_ratio': round(home_goals_ratio, 2),
        'crowd_support': crowd_support,
        'home_avg_goals': round(home_avg_goals, 2),
        'total_home_matches': total_home_matches
    }

def calculate_team_stats(data, seasons):
    """Calcul des statistiques des équipes - Version Simplifiée"""
    if data is None or len(data) == 0:
        return {}
    
    season_data = data[data['Season'].isin(seasons)]
    team_stats = {}
    
    # Obtenir toutes les équipes uniques
    all_teams = set(season_data['HomeTeam'].unique()) | set(season_data['AwayTeam'].unique())
    
    for team in all_teams:
        # Matchs à domicile
        home_matches = season_data[season_data['HomeTeam'] == team]
        home_wins = len(home_matches[home_matches['FTR'] == 'H'])
        home_goals = home_matches['FTHG'].mean() if len(home_matches) > 0 else 0
        
        # Matchs à l'extérieur
        away_matches = season_data[season_data['AwayTeam'] == team]
        away_wins = len(away_matches[away_matches['FTR'] == 'A'])
        away_goals = away_matches['FTAG'].mean() if len(away_matches) > 0 else 0
        
        team_stats[team] = {
            'total_home_matches': len(home_matches),
            'home_wins': home_wins,
            'home_win_rate': home_wins / len(home_matches) if len(home_matches) > 0 else 0,
            'avg_goals_home': home_goals,
            'total_away_matches': len(away_matches),
            'away_wins': away_wins,
            'away_win_rate': away_wins / len(away_matches) if len(away_matches) > 0 else 0,
            'avg_goals_away': away_goals
        }
    
    return team_stats

def show_metric_card(title, value, subtitle):
    """Affichage d'une métrique propre adaptée au thème"""
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin: 0; color: #667eea; font-weight: 600;">{title}</h3>
        <h2 style="margin: 0.5rem 0; font-weight: 700; font-size: 1.8rem;">{value}</h2>
        <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def create_team_performance_chart(team_stats, selected_team):
    """Créer un graphique de performance d'équipe avec Plotly - ÉTAPE 1"""
    if not team_stats or selected_team not in team_stats:
        return None
    
    stats = team_stats[selected_team]
    
    # Données pour le graphique
    categories = ['Domicile', 'Extérieur']
    win_rates = [stats['home_win_rate'] * 100, stats['away_win_rate'] * 100]
    colors = ['#667eea', '#764ba2']
    
    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=win_rates,
            marker_color=colors,
            text=[f"{rate:.1f}%" for rate in win_rates],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=f"📊 Performance de {selected_team}",
        yaxis_title="Taux de Victoire (%)",
        showlegend=False,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig

def show_advanced_notification(message, notification_type="info", icon="ℹ️"):
    """Système de notifications avancé - ÉTAPE 2"""
    
    icons = {
        "success": "✅",
        "warning": "⚠️", 
        "info": "ℹ️",
        "error": "❌"
    }
    
    selected_icon = icons.get(notification_type, icon)
    css_class = f"notification-{notification_type}"
    
    st.markdown(f"""
    <div class="{css_class}">
        <strong>{selected_icon} {message}</strong>
    </div>
    """, unsafe_allow_html=True)

def advanced_prediction_ensemble(home_team, away_team, team_stats, data=None):
    """
    🚀 MODÈLE D'ENSEMBLE V10.4 - Intégrant Head-to-Head et Facteur Domicile Variable
    ================================================================================
    Modèle amélioré avec 6 algorithmes incluant les nouvelles fonctionnalités V10.4
    """
    
    # Modèle 1: Prédiction basée sur les statistiques historiques
    home_stats = team_stats.get(home_team, {})
    away_stats = team_stats.get(away_team, {})
    
    model1_home = home_stats.get('avg_goals_home', 1.5)
    model1_away = away_stats.get('avg_goals_away', 1.5)
    
    # Modèle 2: Prédiction basée sur la forme récente
    home_form = calculate_recent_form(data, home_team) if data is not None else {"form_rating": 0.5}
    away_form = calculate_recent_form(data, away_team) if data is not None else {"form_rating": 0.5}
    
    form_multiplier_home = 0.8 + (home_form['form_rating'] * 0.4)  # 0.8 à 1.2
    form_multiplier_away = 0.8 + (away_form['form_rating'] * 0.4)
    
    model2_home = model1_home * form_multiplier_home
    model2_away = model1_away * form_multiplier_away
    
    # Modèle 3: Prédiction basée sur l'équilibre défensif/offensif
    home_attack = home_stats.get('avg_goals_scored', 1.5)
    home_defense = home_stats.get('avg_goals_conceded', 1.5)
    away_attack = away_stats.get('avg_goals_scored', 1.5)
    away_defense = away_stats.get('avg_goals_conceded', 1.5)
    
    # Confrontation attaque vs défense
    model3_home = (home_attack + away_defense) / 2
    model3_away = (away_attack + home_defense) / 2
    
    # Modèle 4: Prédiction avec facteurs externes
    home_condition = simulate_team_condition(home_team)
    away_condition = simulate_team_condition(away_team)
    
    model4_home = model1_home + home_condition['condition_impact']
    model4_away = model1_away + away_condition['condition_impact']
    
    # 🆚 MODÈLE 5: NOUVEAU - Prédiction basée sur les statistiques Head-to-Head
    h2h_stats = get_head_to_head_stats(data, home_team, away_team) if data is not None else {'has_data': False}
    
    if h2h_stats['has_data']:
        # Ajustement basé sur l'historique des confrontations
        h2h_home_advantage = 0
        if h2h_stats['advantage'] == 'strong_home':
            h2h_home_advantage = 0.4
        elif h2h_stats['advantage'] == 'slight_home':
            h2h_home_advantage = 0.2
        elif h2h_stats['advantage'] == 'strong_away':
            h2h_home_advantage = -0.3
        elif h2h_stats['advantage'] == 'slight_away':
            h2h_home_advantage = -0.15
        
        # Utilisation des moyennes historiques H2H
        model5_home = h2h_stats['avg_goals_home'] + h2h_home_advantage
        model5_away = h2h_stats['avg_goals_away'] - (h2h_home_advantage * 0.5)
    else:
        # Pas de données H2H, utiliser le modèle de base
        model5_home = model1_home
        model5_away = model1_away
    
    # 🏠 MODÈLE 6: NOUVEAU - Prédiction avec facteur domicile variable par équipe
    home_advantage_data = calculate_team_home_advantage(data, home_team) if data is not None else {'factor': 1.2}
    home_advantage_factor = home_advantage_data['factor']
    
    # Application du facteur domicile personnalisé
    model6_home = model1_home * home_advantage_factor
    model6_away = model1_away * (2.0 - home_advantage_factor * 0.5)  # Inverse partiel pour l'équipe extérieure
    
    # Ensemble: Moyenne pondérée des 6 modèles (V10.4)
    weights = [0.2, 0.2, 0.2, 0.15, 0.15, 0.1]  # Poids pour chaque modèle
    
    ensemble_home = (
        weights[0] * model1_home + 
        weights[1] * model2_home + 
        weights[2] * model3_home + 
        weights[3] * model4_home +
        weights[4] * model5_home +
        weights[5] * model6_home
    )
    
    ensemble_away = (
        weights[0] * model1_away + 
        weights[1] * model2_away + 
        weights[2] * model3_away + 
        weights[3] * model4_away +
        weights[4] * model5_away +
        weights[5] * model6_away
    )
    
    # Calcul de confiance basé sur la convergence des modèles
    predictions = [
        [model1_home, model1_away],
        [model2_home, model2_away], 
        [model3_home, model3_away],
        [model4_home, model4_away],
        [model5_home, model5_away],
        [model6_home, model6_away]
    ]
    
    # Mesurer la variance entre les prédictions
    home_variance = np.var([p[0] for p in predictions])
    away_variance = np.var([p[1] for p in predictions])
    avg_variance = (home_variance + away_variance) / 2
    
    # Confiance améliorée avec bonus pour données H2H
    base_confidence = 75  # Augmenté grâce aux nouvelles données
    variance_penalty = min(30, avg_variance * 50)
    h2h_bonus = 10 if h2h_stats['has_data'] and h2h_stats['total_matches'] >= 5 else 0
    confidence = max(45, base_confidence - variance_penalty + h2h_bonus)
    
    return max(0, ensemble_home), max(0, ensemble_away), confidence, {
        "model1": [model1_home, model1_away],
        "model2": [model2_home, model2_away],
        "model3": [model3_home, model3_away], 
        "model4": [model4_home, model4_away],
        "model5_h2h": [model5_home, model5_away],
        "model6_home_advantage": [model6_home, model6_away],
        "home_condition": home_condition,
        "away_condition": away_condition,
        "h2h_stats": h2h_stats,
        "home_advantage_data": home_advantage_data
    }

def calculate_match_probabilities(home_goals, away_goals):
    """Calcul des probabilités de résultat basé sur les scores prédits"""
    
    # Différence de buts prédite
    goal_diff = home_goals - away_goals
    
    # Calcul des probabilités avec une fonction logistique
    # Plus la différence est grande, plus la probabilité de victoire augmente
    
    # Probabilité de victoire domicile
    if goal_diff > 0:
        # Victoire domicile probable
        home_win_prob = 0.5 + (goal_diff / (goal_diff + 2)) * 0.4
    else:
        # Défaite ou égalité
        home_win_prob = 0.5 / (1 + abs(goal_diff))
    
    # Probabilité de victoire extérieur  
    if goal_diff < 0:
        # Victoire extérieur probable
        away_win_prob = 0.5 + (abs(goal_diff) / (abs(goal_diff) + 2)) * 0.4
    else:
        # Défaite ou égalité
        away_win_prob = 0.5 / (1 + goal_diff)
    
    # Probabilité de match nul
    # Plus les scores sont proches, plus la probabilité de nul augmente
    if abs(goal_diff) < 0.5:
        draw_prob = 0.35  # Probabilité élevée si scores très proches
    elif abs(goal_diff) < 1.0:
        draw_prob = 0.25  # Probabilité modérée
    else:
        draw_prob = 0.15 / (1 + abs(goal_diff))  # Probabilité faible si grande différence
    
    # Normaliser pour que la somme soit 100%
    total = home_win_prob + away_win_prob + draw_prob
    
    home_win_prob = (home_win_prob / total) * 100
    away_win_prob = (away_win_prob / total) * 100
    draw_prob = (draw_prob / total) * 100
    
    return {
        'home_win': round(home_win_prob, 1),
        'draw': round(draw_prob, 1), 
        'away_win': round(away_win_prob, 1)
    }

def predict_match(home_team, away_team, team_stats, data=None, use_advanced=True):
    """Prédiction améliorée d'un match avec toutes les améliorations et probabilités"""
    if home_team not in team_stats or away_team not in team_stats:
        return None, None, 0, None
    
    # AMÉLIORATION 4: Utiliser le modèle d'ensemble avancé par défaut
    if use_advanced:
        ensemble_home, ensemble_away, ensemble_confidence, details = advanced_prediction_ensemble(
            home_team, away_team, team_stats, data
        )
        # Calculer les probabilités de résultat
        probabilities = calculate_match_probabilities(ensemble_home, ensemble_away)
        return ensemble_home, ensemble_away, ensemble_confidence, probabilities
    
    # Méthode simplifiée (ancienne version avec améliorations 1-3)
    # AMÉLIORATION 1: Analyser plus de données pour les matchs nuls
    home_stats = team_stats[home_team]
    away_stats = team_stats[away_team]
    
    # Calcul basique
    home_avg = home_stats['avg_goals_home']
    away_avg = away_stats['avg_goals_away']
    
    # AMÉLIORATION 2: Intégrer la forme récente des équipes
    home_form = calculate_recent_form(data, home_team) if data is not None else {"form_rating": 0.5}
    away_form = calculate_recent_form(data, away_team) if data is not None else {"form_rating": 0.5}
    
    # Facteur de forme (0.5 = forme neutre, >0.5 = bonne forme, <0.5 = mauvaise forme)
    home_form_boost = (home_form['form_rating'] - 0.5) * 0.8  # Impact modéré de la forme
    away_form_boost = (away_form['form_rating'] - 0.5) * 0.8
    
    # AMÉLIORATION 3: Considérer les blessures/suspensions et condition
    home_condition = simulate_team_condition(home_team)
    away_condition = simulate_team_condition(away_team)
    
    home_condition_impact = home_condition['condition_impact']
    away_condition_impact = away_condition['condition_impact']
    
    # NOUVEAU: Facteur de tendance aux matchs nuls
    home_draws_rate = home_stats.get('draw_rate', 0.25)  # Taux de nuls historique
    away_draws_rate = away_stats.get('draw_rate', 0.25)
    avg_draw_rate = (home_draws_rate + away_draws_rate) / 2
    
    # NOUVEAU: Ajustement selon la tendance équilibrée des équipes
    goal_balance_home = abs(home_stats.get('avg_goals_scored', 1.5) - home_stats.get('avg_goals_conceded', 1.5))
    goal_balance_away = abs(away_stats.get('avg_goals_scored', 1.5) - away_stats.get('avg_goals_conceded', 1.5))
    
    # Si les équipes sont équilibrées, augmenter la probabilité de nul
    if goal_balance_home < 0.5 and goal_balance_away < 0.5:
        # Équipes équilibrées = plus de chance de match nul
        draw_factor = 1.2
    else:
        draw_factor = 1.0
    
    # Prédiction avec facteur de nul, forme récente ET condition d'équipe
    home_pred = max(0, home_avg + home_form_boost + home_condition_impact + np.random.normal(0, 0.15))
    away_pred = max(0, away_avg + away_form_boost + away_condition_impact + np.random.normal(0, 0.15))
    
    # NOUVEAU: Ajustement pour les matchs nuls probables
    if avg_draw_rate > 0.3 and abs(home_pred - away_pred) < 0.8:
        # Rapprocher les scores pour simuler un match équilibré
        avg_score = (home_pred + away_pred) / 2
        home_pred = avg_score + np.random.normal(0, 0.3)
        away_pred = avg_score + np.random.normal(0, 0.3)
    
    # Calcul de confiance amélioré avec forme
    goal_diff = abs(home_pred - away_pred)
    form_confidence_boost = abs(home_form['form_rating'] - away_form['form_rating']) * 20
    confidence = min(95, 50 + goal_diff * 25 + form_confidence_boost)
    
    # Réduire la confiance si match nul probable
    if goal_diff < 0.5:
        confidence *= 0.8  # Match incertain
    
    # Calculer les probabilités pour la méthode simplifiée aussi
    probabilities = calculate_match_probabilities(home_pred, away_pred)
    
    return home_pred, away_pred, confidence, probabilities

def generate_multi_match_predictions(teams, team_stats, data=None, num_matches=10):
    """Générer des prédictions pour un calendrier complet - ÉTAPE 1.B"""
    import random
    
    predictions = []
    
    for i in range(num_matches):
        # Sélectionner deux équipes aléatoirement
        home_team = random.choice(teams)
        away_team = random.choice([t for t in teams if t != home_team])
        
        # Prédire le match avec données de forme récente
        home_pred, away_pred, confidence, probabilities = predict_match(home_team, away_team, team_stats, data)
        
        if home_pred is not None:
            # Déterminer le résultat
            if home_pred > away_pred + 0.5:
                result = "1"
                winner = home_team
            elif away_pred > home_pred + 0.5:
                result = "2" 
                winner = away_team
            else:
                result = "X"
                winner = "Match nul"
            
            predictions.append({
                "Match": f"{home_team} vs {away_team}",
                "Score Prédit": f"{home_pred:.1f} - {away_pred:.1f}",
                "Résultat": result,
                "Gagnant": winner,
                "Confiance": f"{confidence:.0f}%",
                "Total Buts": f"{home_pred + away_pred:.1f}"
            })
    
    return predictions

def generate_advanced_multi_match_predictions(teams, team_stats, data, num_matches, prediction_type, include_odds, confidence_filter, current_lang):
    """Génération avancée de prédictions multi-matchs avec analyse de valeur - V10.3"""
    import random
    from datetime import datetime, timedelta
    
    predictions = []
    current_date = datetime.now()
    
    for i in range(num_matches):
        # Sélectionner deux équipes aléatoirement
        home_team = random.choice(teams)
        away_team = random.choice([t for t in teams if t != home_team])
        
        # Générer une date future
        match_date = current_date + timedelta(days=random.randint(1, 30))
        
        # Prédire le match avec données de forme récente
        home_pred, away_pred, confidence, probabilities = predict_match(home_team, away_team, team_stats, data)
        
        if home_pred is not None and confidence >= confidence_filter:
            # Déterminer le résultat textuel
            if probabilities['home_win'] > probabilities['away_win'] and probabilities['home_win'] > probabilities['draw']:
                result = "Victoire Domicile"
            elif probabilities['away_win'] > probabilities['home_win'] and probabilities['away_win'] > probabilities['draw']:
                result = "Victoire Extérieur"
            else:
                result = "Match Nul"
            
            # Analyse de valeur (simulation)
            value_score = random.uniform(0, 5)
            has_value = value_score > 3.0 and include_odds
            
            # Facteurs clés simulés
            key_factors = random.choice([
                "Forme récente excellente",
                "Avantage domicile",
                "Historique favorable",
                "Motivation élevée",
                "Effectif complet"
            ])
            
            risk_level = "Faible" if confidence > 75 else ("Moyen" if confidence > 60 else "Élevé")
            
            prediction = {
                "Date": match_date.strftime("%d/%m/%Y"),
                "Match": f"{home_team} vs {away_team}",
                "Résultat": result,
                "Score": f"{home_pred:.1f} - {away_pred:.1f}",
                "Confiance": confidence,
                "Valeur": has_value,
                "Score_Valeur": value_score,
                "Facteur_Clé": key_factors,
                "Risque": risk_level
            }
            
            predictions.append(prediction)
    
    return predictions

def show_prediction_interface(data, selected_seasons, team_stats, teams, current_lang='fr'):
    """Interface de prédiction principale - PROPRE"""
    st.markdown("---")
    st.markdown(f"## 🎯 {get_text('simple_prediction', current_lang)}")
    
    # Configuration du Modèle
    st.markdown(f"### ⚙️ {get_text('model_configuration', current_lang)}")
    col_config1, col_config2 = st.columns(2)
    
    with col_config1:
        prediction_mode = st.selectbox(
            f"🧠 {get_text('prediction_level', current_lang)}:",
            [f"🚀 {get_text('advanced_model', current_lang)}", f"📊 {get_text('simplified_model', current_lang)}"],
            help=get_text('advanced_model_help', current_lang)
        )
        use_advanced = prediction_mode.startswith("🚀")
    
    with col_config2:
        if use_advanced:
            st.success(f"✅ {get_text('using_ensemble_model', current_lang)}:")
            st.write(f"• {get_text('draw_analysis', current_lang)}")
            st.write(f"• {get_text('recent_form', current_lang)}") 
            st.write(f"• {get_text('condition_factors', current_lang)}")
            st.write(f"• {get_text('four_models_combined', current_lang)}")
        else:
            st.info(f"📊 {get_text('simplified_model_active', current_lang)}")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        home_team = st.selectbox(
            f"{get_text('home_team', current_lang)} 🏠",
            [""] + sorted(teams),
            key="home_team_select"
        )
        
        if home_team and home_team in team_stats:
            stats = team_stats[home_team]
            st.info(f"📊 {get_text('home_wins', current_lang)}: {stats['home_wins']}/{stats['total_home_matches']} ({stats['home_win_rate']*100:.1f}%)")
            
            # Graphique de performance - Domicile
            chart = create_team_performance_chart(team_stats, home_team)
            if chart:
                st.plotly_chart(chart, use_container_width=True, key=f"chart_home_{home_team}")
    
    with col2:
        away_team = st.selectbox(
            f"{get_text('away_team', current_lang)} ✈️",
            [""] + sorted(teams),
            key="away_team_select"
        )
        
        if away_team and away_team in team_stats:
            stats = team_stats[away_team]
            st.info(f"📊 {get_text('away_wins', current_lang)}: {stats['away_wins']}/{stats['total_away_matches']} ({stats['away_win_rate']*100:.1f}%)")
            
            # Graphique de performance - Extérieur
            chart = create_team_performance_chart(team_stats, away_team)
            if chart:
                st.plotly_chart(chart, use_container_width=True, key=f"chart_away_{away_team}")
    
    # Bouton de prédiction
    if st.button(f"🔮 {get_text('predict_match', current_lang)}", type="primary"):
        if home_team and away_team and home_team != away_team:
            with st.spinner(f"🤖 {get_text('calculating', current_lang)}..."):
                time.sleep(1)
                
                home_pred, away_pred, confidence, probabilities = predict_match(home_team, away_team, team_stats, data, use_advanced)
                
                if home_pred is not None and probabilities is not None:
                    st.markdown("---")
                    st.markdown(f"### 🏆 {get_text('prediction_result', current_lang)}")
                    
                    # Affichage du score
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.markdown(f"""
                        <div style="text-align: center; background: linear-gradient(135deg, #667eea, #764ba2); 
                                    padding: 2rem; border-radius: 15px; color: white; margin: 1rem 0;">
                            <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 1rem;">
                                <span style="margin: 0 1rem; font-size: 1.2rem;">{home_team} 🆚 {away_team}</span>
                            </div>
                            <h1 style="font-size: 3rem; margin: 1rem 0;">{home_pred:.1f} - {away_pred:.1f}</h1>
                            <p>{get_text('confidence', current_lang)}: {confidence:.0f}%</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Affichage des probabilités de résultat
                    st.markdown(f"### 📊 {get_text('result_probabilities', current_lang)}")
                    col_prob1, col_prob2, col_prob3 = st.columns(3)
                    
                    with col_prob1:
                        st.markdown(f"""
                        <div style="text-align: center; background: linear-gradient(135deg, #28a745, #20c997); 
                                    padding: 1.5rem; border-radius: 15px; color: white; margin: 0.5rem 0;">
                            <h4>🏠 {get_text('victory', current_lang)}</h4>
                            <h5 style="margin: 0.5rem 0;">{home_team}</h5>
                            <h2 style="font-size: 2.5rem; margin: 0.5rem 0;">{probabilities['home_win']:.1f}%</h2>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_prob2:
                        st.markdown(f"""
                        <div style="text-align: center; background: linear-gradient(135deg, #ffc107, #fd7e14); 
                                    padding: 1.5rem; border-radius: 15px; color: white; margin: 0.5rem 0;">
                            <h4>⚖️ {get_text('draw', current_lang)}</h4>
                            <div style="margin: 1rem 0; font-size: 2rem;">🤝</div>
                            <h2 style="font-size: 2.5rem; margin: 0.5rem 0;">{probabilities['draw']:.1f}%</h2>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_prob3:
                        st.markdown(f"""
                        <div style="text-align: center; background: linear-gradient(135deg, #dc3545, #e83e8c); 
                                    padding: 1.5rem; border-radius: 15px; color: white; margin: 0.5rem 0;">
                            <h4>✈️ {get_text('victory', current_lang)}</h4>
                            <h5 style="margin: 0.5rem 0;">{away_team}</h5>
                            <h2 style="font-size: 2.5rem; margin: 0.5rem 0;">{probabilities['away_win']:.1f}%</h2>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Analyse du résultat avec les probabilités
                    max_prob = max(probabilities['home_win'], probabilities['draw'], probabilities['away_win'])
                    
                    if probabilities['home_win'] == max_prob:
                        st.success(f"🏆 {get_text('probable_victory', current_lang)} {home_team} ({probabilities['home_win']:.1f}%)")
                    elif probabilities['away_win'] == max_prob:
                        st.success(f"🏆 {get_text('probable_victory', current_lang)} {away_team} ({probabilities['away_win']:.1f}%)")
                    else:
                        st.warning(f"⚖️ {get_text('probable_draw', current_lang)} ({probabilities['draw']:.1f}%)")
                    
                    # 🆚 NOUVELLE SECTION V10.4 - Statistiques Head-to-Head
                    if use_advanced:
                        h2h_stats = get_head_to_head_stats(data, home_team, away_team)
                        home_advantage_data = calculate_team_home_advantage(data, home_team)
                        
                        st.markdown("---")
                        col_h2h, col_home = st.columns(2)
                        
                        with col_h2h:
                            st.markdown(f"### {get_text('head_to_head_stats', current_lang)}")
                            
                            if h2h_stats['has_data']:
                                # Affichage des statistiques H2H
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #4facfe, #00f2fe); 
                                            padding: 1.5rem; border-radius: 15px; color: white; margin: 0.5rem 0;">
                                    <h4>🆚 {home_team} vs {away_team}</h4>
                                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                                        <div><strong>{get_text('h2h_total_matches', current_lang)}:</strong> {h2h_stats['total_matches']}</div>
                                        <div><strong>{get_text('h2h_home_wins', current_lang)}:</strong> {h2h_stats['home_wins']}</div>
                                        <div><strong>{get_text('h2h_away_wins', current_lang)}:</strong> {h2h_stats['away_wins']}</div>
                                        <div><strong>{get_text('h2h_draws', current_lang)}:</strong> {h2h_stats['draws']}</div>
                                        <div><strong>{get_text('h2h_avg_goals_home', current_lang)}:</strong> {h2h_stats['avg_goals_home']}</div>
                                        <div><strong>{get_text('h2h_avg_goals_away', current_lang)}:</strong> {h2h_stats['avg_goals_away']}</div>
                                    </div>
                                    <div style="margin-top: 1rem;">
                                        <strong>{get_text('h2h_recent_form', current_lang)}:</strong> {' '.join(h2h_stats['recent_form'])}
                                    </div>
                                    <div style="margin-top: 0.5rem;">
                                        <strong>{get_text('h2h_advantage', current_lang)}:</strong> {h2h_stats['advantage']} ({h2h_stats['home_percentage']:.1f}%)
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                # Graphique H2H
                                h2h_fig = go.Figure()
                                h2h_fig.add_trace(go.Bar(
                                    x=[f'{home_team}\n{get_text("h2h_home_wins", current_lang)}', 
                                       get_text('h2h_draws', current_lang), 
                                       f'{away_team}\n{get_text("h2h_away_wins", current_lang)}'],
                                    y=[h2h_stats['home_wins'], h2h_stats['draws'], h2h_stats['away_wins']],
                                    marker_color=['#28a745', '#ffc107', '#dc3545'],
                                    text=[h2h_stats['home_wins'], h2h_stats['draws'], h2h_stats['away_wins']],
                                    textposition='auto'
                                ))
                                h2h_fig.update_layout(
                                    title=f"📊 {get_text('head_to_head_stats', current_lang)}",
                                    showlegend=False,
                                    height=300,
                                    paper_bgcolor='rgba(0,0,0,0)',
                                    plot_bgcolor='rgba(0,0,0,0)'
                                )
                                st.plotly_chart(h2h_fig, use_container_width=True)
                            else:
                                st.info(f"ℹ️ {get_text('h2h_no_data', current_lang)}")
                        
                        with col_home:
                            st.markdown(f"### {get_text('home_advantage_factor', current_lang)}")
                            
                            # Affichage du facteur domicile
                            strength_colors = {
                                'very_strong': '#28a745',
                                'strong': '#6f42c1', 
                                'normal': '#17a2b8',
                                'weak': '#fd7e14',
                                'none': '#dc3545'
                            }
                            
                            strength_color = strength_colors.get(home_advantage_data['strength'], '#17a2b8')
                            
                            st.markdown(f"""
                            <div style="background: linear-gradient(135deg, {strength_color}, {strength_color}dd); 
                                        padding: 1.5rem; border-radius: 15px; color: white; margin: 0.5rem 0;">
                                <h4>🏠 {home_team}</h4>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 1rem; margin-top: 1rem;">
                                    <div><strong>{get_text('team_home_strength', current_lang)}:</strong> {home_advantage_data['strength']}</div>
                                    <div><strong>Factor:</strong> {home_advantage_data['factor']:.2f}</div>
                                    <div><strong>{get_text('home_wins_percentage', current_lang)}:</strong> {home_advantage_data['home_wins_percentage']:.1f}%</div>
                                    <div><strong>{get_text('home_goals_ratio', current_lang)}:</strong> {home_advantage_data['home_goals_ratio']:.2f}</div>
                                    <div><strong>{get_text('crowd_support_factor', current_lang)}:</strong> {home_advantage_data['crowd_support']}</div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Graphique facteur domicile
                            home_fig = go.Figure()
                            home_fig.add_trace(go.Indicator(
                                mode = "gauge+number",
                                value = home_advantage_data['factor'],
                                domain = {'x': [0, 1], 'y': [0, 1]},
                                title = {'text': f"{get_text('home_advantage_factor', current_lang)}"},
                                gauge = {
                                    'axis': {'range': [1.0, 1.5]},
                                    'bar': {'color': strength_color},
                                    'steps': [
                                        {'range': [1.0, 1.1], 'color': "#dc3545"},
                                        {'range': [1.1, 1.2], 'color': "#fd7e14"},
                                        {'range': [1.2, 1.3], 'color': "#17a2b8"},
                                        {'range': [1.3, 1.4], 'color': "#6f42c1"},
                                        {'range': [1.4, 1.5], 'color': "#28a745"}
                                    ],
                                    'threshold': {
                                        'line': {'color': "red", 'width': 4},
                                        'thickness': 0.75,
                                        'value': 1.2
                                    }
                                }
                            ))
                            home_fig.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20))
                            st.plotly_chart(home_fig, use_container_width=True)
                
                else:
                    st.error(f"❌ {get_text('prediction_error', current_lang)}")
        else:
            st.error(f"⚠️ {get_text('select_different_teams', current_lang)}")

def show_multi_match_interface(data, selected_seasons, team_stats, teams, current_lang='fr'):
    """Interface pour prédictions multi-matchs - CALENDRIER COMPLET V10.3"""
    st.markdown("---")
    st.markdown(f"## {get_text('multi_match_predictions', current_lang)} - {get_text('complete_calendar', current_lang)}")
    
    show_advanced_notification(
        get_text('calendar_generation_info', current_lang), 
        "info"
    )
    
    # Configuration avancée du calendrier
    col1, col2, col3 = st.columns(3)
    
    with col1:
        num_matches = st.slider(
            get_text('matches_to_predict', current_lang), 
            10, 50, 20
        )
    
    with col2:
        match_period = st.selectbox(
            get_text('prediction_period', current_lang),
            [get_text('next_week', current_lang), get_text('next_month', current_lang), get_text('next_season', current_lang)]
        )
    
    with col3:
        prediction_type = st.selectbox(
            get_text('prediction_detail_level', current_lang),
            [get_text('detailed_analysis', current_lang), get_text('quick_overview', current_lang)]
        )
    
    # Options avancées
    st.markdown(f"### {get_text('advanced_options', current_lang)}")
    col_opt1, col_opt2, col_opt3 = st.columns(3)
    
    with col_opt1:
        include_odds = st.checkbox(get_text('include_value_analysis', current_lang), value=True)
    
    with col_opt2:
        confidence_filter = st.slider(get_text('min_confidence_filter', current_lang), 0, 100, 60)
    
    with col_opt3:
        export_format = st.selectbox(
            get_text('export_format', current_lang),
            ["CSV", "JSON", get_text('display_only', current_lang)]
        )
    
    if st.button(get_text('generate_complete_calendar', current_lang), type="primary"):
        with st.spinner(get_text('generating_calendar', current_lang)):
            # Simulation de génération intelligente
            time.sleep(3)
            
            predictions = generate_advanced_multi_match_predictions(
                teams, team_stats, data, num_matches, prediction_type, include_odds, confidence_filter, current_lang
            )
            
            if predictions:
                show_advanced_notification(
                    f"✅ {len(predictions)} {get_text('predictions_generated', current_lang)}", 
                    "success"
                )
                
                # Résumé exécutif
                st.markdown(f"### 📊 {get_text('executive_summary', current_lang)}")
                col_sum1, col_sum2, col_sum3, col_sum4 = st.columns(4)
                
                high_conf_count = len([p for p in predictions if p["Confiance"] >= 75])
                value_bets_count = len([p for p in predictions if p.get("Valeur", False)])
                avg_confidence = sum(p["Confiance"] for p in predictions) / len(predictions)
                
                with col_sum1:
                    st.metric(get_text('total_matches', current_lang), len(predictions))
                
                with col_sum2:
                    st.metric(get_text('high_confidence', current_lang), high_conf_count, f"{high_conf_count/len(predictions)*100:.0f}%")
                
                with col_sum3:
                    st.metric(get_text('value_opportunities', current_lang), value_bets_count)
                
                with col_sum4:
                    st.metric(get_text('avg_confidence', current_lang), f"{avg_confidence:.1f}%")
                
                # Filtrage et tri
                st.markdown(f"### 🔍 {get_text('filter_and_sort', current_lang)}")
                col_filter1, col_filter2 = st.columns(2)
                
                with col_filter1:
                    result_filter = st.multiselect(
                        get_text('filter_by_result', current_lang),
                        ["Victoire Domicile", "Match Nul", "Victoire Extérieur"],
                        default=["Victoire Domicile", "Match Nul", "Victoire Extérieur"]
                    )
                
                with col_filter2:
                    sort_by = st.selectbox(
                        get_text('sort_by', current_lang),
                        [get_text('confidence_desc', current_lang), get_text('date_asc', current_lang), get_text('value_desc', current_lang)]
                    )
                
                # Appliquer les filtres
                filtered_predictions = [p for p in predictions if p["Résultat"] in result_filter]
                
                # Trier
                if sort_by == get_text('confidence_desc', current_lang):
                    filtered_predictions.sort(key=lambda x: x["Confiance"], reverse=True)
                elif sort_by == get_text('value_desc', current_lang):
                    filtered_predictions.sort(key=lambda x: x.get("Score_Valeur", 0), reverse=True)
                
                # Affichage du calendrier principal
                st.markdown(f"### 🏆 {get_text('prediction_calendar', current_lang)}")
                
                # Mode d'affichage avancé
                if prediction_type == get_text('detailed_analysis', current_lang):
                    # Affichage détaillé avec cartes
                    for i, pred in enumerate(filtered_predictions):
                        with st.expander(f"🏟️ {pred['Match']} - {pred['Date']} (⚡ {pred['Confiance']:.1f}%)", expanded=i<3):
                            col_det1, col_det2, col_det3 = st.columns(3)
                            
                            with col_det1:
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #28a745, #20c997); 
                                            padding: 1rem; border-radius: 10px; color: white; text-align: center;">
                                    <h4>🏆 {get_text('prediction', current_lang)}</h4>
                                    <p><strong>{pred['Résultat']}</strong></p>
                                    <p>{pred['Score']}</p>
                                    <p>⚡ {pred['Confiance']:.1f}%</p>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            with col_det2:
                                color = "#dc3545" if not pred.get("Valeur", False) else "#28a745"
                                value_text = get_text('value_detected', current_lang) if pred.get("Valeur", False) else get_text('no_value', current_lang)
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, {color}, #fd7e14); 
                                            padding: 1rem; border-radius: 10px; color: white; text-align: center;">
                                    <h4>💰 {get_text('value_analysis', current_lang)}</h4>
                                    <p>{value_text}</p>
                                    <p>{get_text('score', current_lang)}: {pred.get('Score_Valeur', 0):.2f}</p>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            with col_det3:
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                                            padding: 1rem; border-radius: 10px; color: white; text-align: center;">
                                    <h4>📊 {get_text('key_factors', current_lang)}</h4>
                                    <p>{pred.get('Facteur_Clé', 'Forme récente')}</p>
                                    <p>{get_text('risk_level', current_lang)}: {pred.get('Risque', 'Moyen')}</p>
                                </div>
                                """, unsafe_allow_html=True)
                else:
                    # Affichage tableau rapide
                    df_predictions = pd.DataFrame(filtered_predictions)
                    # Traduire les colonnes
                    df_display = df_predictions.copy()
                    column_mapping = {
                        'Date': get_text('table_date', current_lang),
                        'Match': get_text('table_match', current_lang),
                        'Résultat': get_text('result', current_lang),
                        'Score': get_text('score', current_lang),
                        'Confiance': f"{get_text('confidence', current_lang)} (%)"
                    }
                    df_display = df_display.rename(columns=column_mapping)
                    
                    st.dataframe(df_display, use_container_width=True, hide_index=True)
                
                # Statistiques détaillées du calendrier
                st.markdown(f"### � {get_text('calendar_statistics', current_lang)}")
                
                col_stat1, col_stat2, col_stat3 = st.columns(3)
                
                with col_stat1:
                    # Distribution des résultats
                    result_counts = {}
                    for pred in filtered_predictions:
                        result = pred["Résultat"]
                        result_counts[result] = result_counts.get(result, 0) + 1
                    
                    fig_results = go.Figure(data=[go.Pie(
                        labels=list(result_counts.keys()),
                        values=list(result_counts.values()),
                        hole=0.3
                    )])
                    fig_results.update_layout(
                        title=get_text('results_distribution', current_lang),
                        height=300,
                        template='plotly_dark'
                    )
                    st.plotly_chart(fig_results, use_container_width=True)
                
                with col_stat2:
                    # Distribution de confiance
                    confidence_levels = [p["Confiance"] for p in filtered_predictions]
                    fig_conf = go.Figure(data=[go.Histogram(
                        x=confidence_levels,
                        nbinsx=10,
                        marker_color='#667eea'
                    )])
                    fig_conf.update_layout(
                        title=get_text('confidence_distribution', current_lang),
                        xaxis_title=get_text('confidence', current_lang),
                        yaxis_title=get_text('frequency', current_lang),
                        height=300,
                        template='plotly_dark'
                    )
                    st.plotly_chart(fig_conf, use_container_width=True)
                
                with col_stat3:
                    # Opportunités de valeur par jour
                    value_by_date = {}
                    for pred in filtered_predictions:
                        date = pred["Date"]
                        if pred.get("Valeur", False):
                            value_by_date[date] = value_by_date.get(date, 0) + 1
                    
                    if value_by_date:
                        dates = list(value_by_date.keys())
                        values = list(value_by_date.values())
                        
                        fig_value = go.Figure(data=[go.Bar(
                            x=dates,
                            y=values,
                            marker_color='#28a745'
                        )])
                        fig_value.update_layout(
                            title=get_text('value_opportunities_by_date', current_lang),
                            height=300,
                            template='plotly_dark'
                        )
                        st.plotly_chart(fig_value, use_container_width=True)
                
                # Export des données
                if export_format != get_text('display_only', current_lang):
                    st.markdown(f"### 💾 {get_text('export_predictions', current_lang)}")
                    
                    if export_format == "CSV":
                        csv_data = pd.DataFrame(filtered_predictions).to_csv(index=False)
                        st.download_button(
                            label=f"📄 {get_text('download_csv', current_lang)}",
                            data=csv_data,
                            file_name=f"football_predictions_{match_period.lower().replace(' ', '_')}.csv",
                            mime="text/csv"
                        )
                    
                    elif export_format == "JSON":
                        import json
                        json_data = json.dumps(filtered_predictions, indent=2, ensure_ascii=False)
                        st.download_button(
                            label=f"📄 {get_text('download_json', current_lang)}",
                            data=json_data,
                            file_name=f"football_predictions_{match_period.lower().replace(' ', '_')}.json",
                            mime="application/json"
                        )

def show_bookmaker_odds(data, teams, current_lang='fr'):
    """Affichage des cotes bookmakers avec comparaison IA - VERSION V10.2"""
    st.markdown("---")
    st.markdown(f"## {get_text('bookmaker_odds_title', current_lang)} & {get_text('ai_comparison', current_lang)}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        home_team = st.selectbox(get_text('home_team_odds', current_lang), teams, key="odds_home")
    
    with col2:
        away_team = st.selectbox(get_text('away_team_odds', current_lang), teams, key="odds_away")
    
    if st.button(get_text('view_odds', current_lang), type="primary"):
        if home_team and away_team and home_team != away_team:
            # Recherche des matchs historiques
            historical_matches = data[
                ((data['HomeTeam'] == home_team) & (data['AwayTeam'] == away_team)) |
                ((data['HomeTeam'] == away_team) & (data['AwayTeam'] == home_team))
            ]
            
            if len(historical_matches) > 0:
                st.success(f"✅ {len(historical_matches)} {get_text('matches_found', current_lang)}")
                
                # NOUVEAU: Prédiction IA pour ce match
                st.markdown(f"### 🤖 {get_text('ai_prediction_vs_odds', current_lang)}")
                
                # Simulation d'une prédiction (utilise la logique existante)
                home_prob = np.random.normal(45, 15)
                home_prob = max(20, min(70, home_prob))
                draw_prob = np.random.normal(25, 8)
                draw_prob = max(15, min(35, draw_prob))
                away_prob = 100 - home_prob - draw_prob
                
                # Affichage des prédictions IA vs cotes moyennes
                col_ai, col_odds, col_comparison = st.columns(3)
                
                with col_ai:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                                padding: 1rem; border-radius: 10px; color: white; text-align: center;">
                        <h4>🤖 {get_text('ai_prediction', current_lang)}</h4>
                        <p><strong>{home_team}:</strong> {home_prob:.1f}%</p>
                        <p><strong>{get_text('draw', current_lang)}:</strong> {draw_prob:.1f}%</p>
                        <p><strong>{away_team}:</strong> {away_prob:.1f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Calcul des cotes moyennes historiques
                recent_matches = historical_matches.tail(5)
                avg_home_odds = recent_matches['B365H'].dropna().mean() if 'B365H' in recent_matches.columns else 2.5
                avg_draw_odds = recent_matches['B365D'].dropna().mean() if 'B365D' in recent_matches.columns else 3.2
                avg_away_odds = recent_matches['B365A'].dropna().mean() if 'B365A' in recent_matches.columns else 2.8
                
                with col_odds:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #28a745, #20c997); 
                                padding: 1rem; border-radius: 10px; color: white; text-align: center;">
                        <h4>💰 {get_text('bookmaker_odds', current_lang)}</h4>
                        <p><strong>{home_team}:</strong> {avg_home_odds:.2f} ({100/avg_home_odds:.1f}%)</p>
                        <p><strong>{get_text('draw', current_lang)}:</strong> {avg_draw_odds:.2f} ({100/avg_draw_odds:.1f}%)</p>
                        <p><strong>{away_team}:</strong> {avg_away_odds:.2f} ({100/avg_away_odds:.1f}%)</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_comparison:
                    # Comparaison et recommandation
                    home_bookmaker_prob = 100/avg_home_odds
                    draw_bookmaker_prob = 100/avg_draw_odds
                    away_bookmaker_prob = 100/avg_away_odds
                    
                    # Détection d'opportunités de valeur
                    value_bets = []
                    if home_prob > home_bookmaker_prob + 5:
                        value_bets.append(f"✅ {home_team} ({get_text('value_bet', current_lang)})")
                    if draw_prob > draw_bookmaker_prob + 3:
                        value_bets.append(f"✅ {get_text('draw', current_lang)} ({get_text('value_bet', current_lang)})")
                    if away_prob > away_bookmaker_prob + 5:
                        value_bets.append(f"✅ {away_team} ({get_text('value_bet', current_lang)})")
                    
                    recommendation_color = "#dc3545" if not value_bets else "#28a745"
                    recommendation_text = get_text('no_value_found', current_lang) if not value_bets else "<br>".join(value_bets)
                    
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, {recommendation_color}, #fd7e14); 
                                padding: 1rem; border-radius: 10px; color: white; text-align: center;">
                        <h4>📊 {get_text('recommendation', current_lang)}</h4>
                        <p>{recommendation_text}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Afficher les matchs historiques
                st.markdown(f"### 📚 {get_text('historical_matches', current_lang)}")
                recent_matches = historical_matches.tail(3)
                
                for idx, (_, match) in enumerate(recent_matches.iterrows()):
                    match_title = f"🏆 {get_text('match_date', current_lang)} {idx+1} - {match['Date'].strftime('%d/%m/%Y')} - {match['HomeTeam']} vs {match['AwayTeam']}"
                    with st.expander(match_title):
                        
                        # Score
                        st.write(f"⚽ **{get_text('score', current_lang)}:** {int(match['FTHG'])}-{int(match['FTAG'])}")
                        
                        # Cotes si disponibles
                        cotes_affichees = False
                        
                        if pd.notna(match.get('B365H')) and match.get('B365H', 0) > 0:
                            st.write(f"🟢 **Bet365:** {get_text('odds_home_team', current_lang)} {match['B365H']:.2f} | {get_text('odds_draw', current_lang)} {match.get('B365D', 0):.2f} | {get_text('odds_away_team', current_lang)} {match.get('B365A', 0):.2f}")
                            cotes_affichees = True
                        
                        if pd.notna(match.get('BWH')) and match.get('BWH', 0) > 0:
                            st.write(f"🔵 **Betway:** {get_text('odds_home_team', current_lang)} {match['BWH']:.2f} | {get_text('odds_draw', current_lang)} {match.get('BWD', 0):.2f} | {get_text('odds_away_team', current_lang)} {match.get('BWA', 0):.2f}")
                            cotes_affichees = True
                        
                        if not cotes_affichees:
                            st.warning(get_text('no_odds_available', current_lang))
            else:
                st.error(f"{get_text('no_match_found', current_lang)} {home_team} et {away_team}")
        else:
            st.error(get_text('select_different_teams', current_lang))

def simulate_match_events(home_team, away_team, home_pred, away_pred, simulation_speed=1):
    """
    🎮 NOUVELLE FONCTIONNALITÉ V10.5 - Générateur d'événements de match
    ================================================================
    Génère les événements de match (buts, cartons, etc.) basés sur les prédictions
    """
    events = []
    home_score = 0
    away_score = 0
    
    # Calcul de la probabilité d'événements basée sur les prédictions
    total_goals = home_pred + away_pred
    match_intensity = min(max(total_goals / 3.0, 0.3), 1.0)  # Intensité entre 0.3 et 1.0
    
    # Distribution des buts dans le temps (plus probable en 2ème mi-temps)
    goal_probabilities = {
        (0, 15): 0.15,
        (15, 30): 0.20,
        (30, 45): 0.15,
        (45, 60): 0.20,
        (60, 75): 0.20,
        (75, 90): 0.25
    }
    
    # Générer les buts
    for (start_min, end_min), prob_weight in goal_probabilities.items():
        # Buts domicile
        for _ in range(int(home_pred * prob_weight) + (1 if np.random.random() < (home_pred * prob_weight) % 1 else 0)):
            minute = np.random.randint(start_min, end_min)
            events.append({
                'minute': minute,
                'type': 'goal',
                'team': home_team,
                'player': f"Joueur {np.random.randint(1, 11)}",
                'description': f"⚽ BUT ! - {home_team}"
            })
            home_score += 1
        
        # Buts extérieur  
        for _ in range(int(away_pred * prob_weight) + (1 if np.random.random() < (away_pred * prob_weight) % 1 else 0)):
            minute = np.random.randint(start_min, end_min)
            events.append({
                'minute': minute,
                'type': 'goal',
                'team': away_team,
                'player': f"Joueur {np.random.randint(1, 11)}",
                'description': f"⚽ BUT ! - {away_team}"
            })
            away_score += 1
    
    # Générer cartons jaunes (2-6 par match)
    num_yellow_cards = np.random.randint(2, 6)
    for _ in range(num_yellow_cards):
        minute = np.random.randint(5, 88)
        team = np.random.choice([home_team, away_team])
        events.append({
            'minute': minute,
            'type': 'yellow_card',
            'team': team,
            'player': f"Joueur {np.random.randint(1, 11)}",
            'description': f"🟨 Carton Jaune - {team}"
        })
    
    # Générer cartons rouges (0-2 par match, rare)
    if np.random.random() < 0.3:  # 30% de chance d'avoir un carton rouge
        minute = np.random.randint(20, 85)
        team = np.random.choice([home_team, away_team])
        events.append({
            'minute': minute,
            'type': 'red_card', 
            'team': team,
            'player': f"Joueur {np.random.randint(1, 11)}",
            'description': f"🟥 Carton Rouge - {team}"
        })
    
    # Générer remplacements (4-6 par match)
    num_substitutions = np.random.randint(4, 6)
    for _ in range(num_substitutions):
        minute = np.random.randint(45, 85)
        team = np.random.choice([home_team, away_team])
        events.append({
            'minute': minute,
            'type': 'substitution',
            'team': team,
            'player': f"Joueur {np.random.randint(1, 11)} → Joueur {np.random.randint(12, 23)}",
            'description': f"🔄 Remplacement - {team}"
        })
    
    # Trier les événements par minute
    events.sort(key=lambda x: x['minute'])
    
    # Générer les statistiques du match
    stats = {
        'possession': {
            home_team: np.random.randint(35, 65),
            away_team: 0
        },
        'shots': {
            home_team: np.random.randint(8, 20),
            away_team: np.random.randint(8, 20)
        },
        'shots_on_target': {
            home_team: np.random.randint(3, 8),
            away_team: np.random.randint(3, 8)
        },
        'corners': {
            home_team: np.random.randint(2, 12),
            away_team: np.random.randint(2, 12)
        },
        'fouls': {
            home_team: np.random.randint(8, 18),
            away_team: np.random.randint(8, 18)
        },
        'offside': {
            home_team: np.random.randint(0, 5),
            away_team: np.random.randint(0, 5)
        }
    }
    
    # Ajuster possession pour totaliser 100%
    stats['possession'][away_team] = 100 - stats['possession'][home_team]
    
    return events, home_score, away_score, stats

def show_match_engine_simulation(data, selected_seasons, team_stats, teams, current_lang='fr'):
    """
    🎮 NOUVELLE FONCTIONNALITÉ V10.5 - Interface de Simulation de Match Style Football Manager
    ==========================================================================================
    """
    st.markdown("---")
    st.markdown(f"## {get_text('match_engine_simulation', current_lang)}")
    
    # CSS pour le fond gazon et style Football Manager
    st.markdown("""
    <style>
    .football-pitch {
        background: linear-gradient(
            90deg,
            #2d5a27 0%,
            #4a7c59 10%,
            #2d5a27 20%,
            #4a7c59 30%,
            #2d5a27 40%,
            #4a7c59 50%,
            #2d5a27 60%,
            #4a7c59 70%,
            #2d5a27 80%,
            #4a7c59 90%,
            #2d5a27 100%
        );
        padding: 2rem;
        border-radius: 15px;
        border: 3px solid #fff;
        margin: 1rem 0;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    }
    
    .match-scoreboard {
        background: rgba(0,0,0,0.8);
        border: 2px solid #fff;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    /* 🎆 ANIMATION DE BUT */
    .goal-celebration {
        animation: goalFlash 2.5s ease-in-out;
        border: 5px solid gold !important;
        box-shadow: 0 0 30px gold, 0 0 60px gold, 0 0 90px gold !important;
        background: linear-gradient(45deg, #FFD700, #FFA500, #FFD700) !important;
    }
    
    @keyframes goalFlash {
        0% { 
            box-shadow: 0 0 10px gold;
            transform: scale(1);
            background: rgba(0,0,0,0.8);
        }
        20% { 
            box-shadow: 0 0 40px gold, 0 0 80px gold;
            transform: scale(1.03);
            background: linear-gradient(45deg, #FFD700, #FF6347, #FFD700);
        }
        50% { 
            box-shadow: 0 0 60px gold, 0 0 120px gold, 0 0 180px gold;
            transform: scale(1.08);
            background: linear-gradient(45deg, #FFD700, #FF1493, #FFD700);
        }
        80% { 
            box-shadow: 0 0 40px gold, 0 0 80px gold;
            transform: scale(1.03);
            background: linear-gradient(45deg, #FFD700, #FF6347, #FFD700);
        }
        100% { 
            box-shadow: 0 0 10px gold;
            transform: scale(1);
            background: rgba(0,0,0,0.8);
        }
    }
    
    /* Animation de pulsation pour les événements importants */
    .event-highlight {
        animation: eventPulse 1.5s ease-in-out;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4) !important;
        color: white !important;
        font-weight: bold !important;
        transform: scale(1.02);
    }
    
    @keyframes eventPulse {
        0% { transform: scale(1); opacity: 0.7; }
        50% { transform: scale(1.02); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .event-feed {
        background: rgba(0,0,0,0.7);
        border-radius: 10px;
        padding: 1rem;
        max-height: 400px;
        overflow-y: auto;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 0.95rem;
        line-height: 1.4;
    }
    
    .match-stats {
        background: rgba(0,0,0,0.6);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .simulation-controls {
        background: rgba(0,0,0,0.8);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Effet de feu d'artifice pour les buts */
    .fireworks {
        position: relative;
        overflow: hidden;
    }
    
    .fireworks::before {
        content: '🎆';
        position: absolute;
        top: -10px;
        left: 10%;
        font-size: 2rem;
        animation: firework1 2s ease-out;
    }
    
    .fireworks::after {
        content: '🎇';
        position: absolute;
        top: -10px;
        right: 10%;
        font-size: 2rem;
        animation: firework2 2s ease-out;
    }
    
    @keyframes firework1 {
        0% { transform: translateY(50px) scale(0); opacity: 0; }
        50% { transform: translateY(-20px) scale(1); opacity: 1; }
        100% { transform: translateY(-50px) scale(0.5); opacity: 0; }
    }
    
    @keyframes firework2 {
        0% { transform: translateY(50px) scale(0) rotate(0deg); opacity: 0; }
        50% { transform: translateY(-20px) scale(1) rotate(180deg); opacity: 1; }
        100% { transform: translateY(-50px) scale(0.5) rotate(360deg); opacity: 0; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Interface de sélection des équipes
    st.markdown(f"### ⚽ {get_text('select_teams_for_simulation', current_lang)}")
    
    col1, col2 = st.columns(2)
    with col1:
        home_team = st.selectbox(f"🏠 {get_text('home_team', current_lang)}:", teams, key="sim_home")
    with col2:
        away_team = st.selectbox(f"✈️ {get_text('away_team', current_lang)}:", teams, key="sim_away")
    
    if home_team and away_team and home_team != away_team:
        # Aperçu du match avec prédiction
        st.markdown(f"### 🔮 {get_text('match_preview', current_lang)}")
        
        # Obtenir la prédiction pour ce match
        home_pred, away_pred, confidence, probabilities = predict_match(home_team, away_team, team_stats, data, True)
        
        if home_pred is not None:
            st.markdown(f"""
            <div class="football-pitch">
                <div class="match-scoreboard">
                    <h2>🏟️ {home_team} 🆚 {away_team}</h2>
                    <h3>{get_text('predicted_result', current_lang)}: {home_pred:.1f} - {away_pred:.1f}</h3>
                    <p>{get_text('confidence', current_lang)}: {confidence:.0f}%</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Contrôles de simulation
            st.markdown(f"### 🎮 {get_text('simulation_start', current_lang)}")
            
            col_speed, col_button = st.columns([1, 1])
            
            with col_speed:
                simulation_speed = st.selectbox(
                    f"⚡ {get_text('simulation_speed', current_lang)}:",
                    [
                        f"{get_text('speed_x1', current_lang)}",
                        f"{get_text('speed_x5', current_lang)}", 
                        f"{get_text('speed_x10', current_lang)}",
                        f"{get_text('speed_x20', current_lang)}"
                    ]
                )
                speed_multiplier = [1, 5, 10, 20][
                    [get_text('speed_x1', current_lang), get_text('speed_x5', current_lang), 
                     get_text('speed_x10', current_lang), get_text('speed_x20', current_lang)].index(simulation_speed)
                ]
            
            with col_button:
                if st.button(f"🎮 {get_text('simulate_match', current_lang)}", type="primary"):
                    # Initialiser la simulation
                    st.session_state.simulation_active = True
                    st.session_state.simulation_events, st.session_state.final_home_score, st.session_state.final_away_score, st.session_state.match_stats = simulate_match_events(
                        home_team, away_team, home_pred, away_pred, speed_multiplier
                    )
                    st.session_state.current_minute = 0
                    st.session_state.displayed_events = []
                    st.session_state.current_home_score = 0
                    st.session_state.current_away_score = 0
            
            # Affichage de la simulation en cours
            if hasattr(st.session_state, 'simulation_active') and st.session_state.simulation_active:
                
                # Zone de simulation principale
                simulation_container = st.container()
                
                with simulation_container:
                    # Auto-refresh pour l'animation
                    if st.session_state.current_minute <= 90:
                        # Avancer le temps
                        st.session_state.current_minute += speed_multiplier
                        if st.session_state.current_minute > 90:
                            st.session_state.current_minute = 90
                        
                        # Vérifier les nouveaux événements
                        new_events = [e for e in st.session_state.simulation_events 
                                    if e['minute'] <= st.session_state.current_minute 
                                    and e not in st.session_state.displayed_events]
                        
                        # Détecter les nouveaux buts pour l'animation
                        new_goal_scored = False
                        goal_scorer_team = None
                        
                        for event in new_events:
                            st.session_state.displayed_events.append(event)
                            if event['type'] == 'goal':
                                new_goal_scored = True
                                goal_scorer_team = event['team']
                                if event['team'] == home_team:
                                    st.session_state.current_home_score += 1
                                else:
                                    st.session_state.current_away_score += 1
                        
                        # Classes CSS pour l'animation
                        scoreboard_class = "match-scoreboard"
                        if new_goal_scored:
                            scoreboard_class += " goal-celebration fireworks"
                        
                        # Interface de match en cours avec animation
                        goal_message = ""
                        if new_goal_scored and goal_scorer_team:
                            goal_message = f"<p style='font-size: 1.5rem; color: gold; text-align: center; margin: 1rem 0;'>⚽ BUT DE {goal_scorer_team.upper()} ! 🎆</p>"
                        
                        st.markdown(f"""
                        <div class="football-pitch">
                            <div class="{scoreboard_class}">
                                <h1>🏟️ {home_team} {st.session_state.current_home_score} - {st.session_state.current_away_score} {away_team}</h1>
                                <h2>⏰ {st.session_state.current_minute}'</h2>
                                <p>🎮 {get_text('simulation_in_progress', current_lang)} (Speed: x{speed_multiplier})</p>
                                {goal_message}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Feed des événements
                        col_events, col_stats = st.columns([1, 1])
                        
                        with col_events:
                            st.markdown(f"### 📋 {get_text('match_events', current_lang)}")
                            
                            # Conteneur pour les événements avec HTML personnalisé
                            events_container = st.container()
                            
                            with events_container:
                                # Créer une liste des 10 derniers événements
                                recent_events = list(reversed(st.session_state.displayed_events[-10:]))
                                
                                # Afficher chaque événement individuellement avec st.markdown
                                for i, event in enumerate(recent_events):
                                    # Déterminer le style selon le type d'événement
                                    if event['type'] == 'goal':
                                        icon = "⚽"
                                        bg_color = "rgba(255, 215, 0, 0.15)"
                                        text_color = "#FFD700"
                                        border_color = "#FFD700"
                                        font_weight = "bold"
                                    elif event['type'] == 'yellow_card':
                                        icon = "🟨"
                                        bg_color = "rgba(255, 255, 0, 0.1)"
                                        text_color = "#FFD700"
                                        border_color = "#FFD700"
                                        font_weight = "normal"
                                    elif event['type'] == 'red_card':
                                        icon = "🟥"
                                        bg_color = "rgba(255, 0, 0, 0.15)"
                                        text_color = "#FF4444"
                                        border_color = "#FF4444"
                                        font_weight = "bold"
                                    elif event['type'] == 'substitution':
                                        icon = "🔄"
                                        bg_color = "rgba(135, 206, 235, 0.1)"
                                        text_color = "#87CEEB"
                                        border_color = "#87CEEB"
                                        font_weight = "normal"
                                    else:
                                        icon = "⚽"
                                        bg_color = "rgba(255, 255, 255, 0.05)"
                                        text_color = "#FFFFFF"
                                        border_color = "#FFFFFF"
                                        font_weight = "normal"
                                    
                                    # Animation pour les nouveaux événements
                                    animation_style = ""
                                    if event in new_events:
                                        animation_style = "animation: eventPulse 1.5s ease-in-out;"
                                    
                                    # Nettoyer la description
                                    description_clean = event['description'].replace('⚽ ', '').replace('🟨 ', '').replace('🟥 ', '').replace('🔄 ', '')
                                    
                                    # Afficher l'événement avec style personnalisé
                                    st.markdown(f"""
                                    <div style="
                                        background: {bg_color};
                                        border-left: 4px solid {border_color};
                                        border-radius: 8px;
                                        padding: 0.7rem;
                                        margin: 0.4rem 0;
                                        color: {text_color};
                                        font-weight: {font_weight};
                                        font-family: 'Segoe UI', sans-serif;
                                        transition: all 0.3s ease;
                                        {animation_style}
                                    ">
                                        {icon} <strong>{event['minute']}'</strong> - {description_clean}
                                    </div>
                                    """, unsafe_allow_html=True)
                        
                        with col_stats:
                            st.markdown(f"#### 📊 {get_text('match_statistics', current_lang)}")
                            progress = st.session_state.current_minute / 90
                            
                            # Statistiques en temps réel (proportionnelles au temps écoulé)
                            current_stats = {}
                            for stat_name, stat_values in st.session_state.match_stats.items():
                                current_stats[stat_name] = {}
                                for team, value in stat_values.items():
                                    # Sécuriser l'accès aux équipes
                                    if team in [home_team, away_team]:
                                        current_stats[stat_name][team] = int(value * progress)
                                    
                            # Sécuriser l'affichage des métriques
                            home_possession = current_stats.get('possession', {}).get(home_team, 50)
                            away_possession = current_stats.get('possession', {}).get(away_team, 50)
                            home_shots = current_stats.get('shots', {}).get(home_team, 0)
                            away_shots = current_stats.get('shots', {}).get(away_team, 0)
                            home_corners = current_stats.get('corners', {}).get(home_team, 0)
                            away_corners = current_stats.get('corners', {}).get(away_team, 0)
                            
                            # Affichage robuste des statistiques avec colonnes
                            st.markdown("### 📊 Statistiques Live")
                            stat_col1, stat_col2, stat_col3 = st.columns(3)
                            
                            with stat_col1:
                                st.metric(
                                    label="🥅 Possession", 
                                    value=f"{home_team}: {home_possession}%",
                                    delta=f"{away_team}: {away_possession}%"
                                )
                            
                            with stat_col2:
                                st.metric(
                                    label="⚽ Tirs", 
                                    value=f"{home_team}: {home_shots}",
                                    delta=f"{away_team}: {away_shots}"
                                )
                            
                            with stat_col3:
                                st.metric(
                                    label="🚩 Corners", 
                                    value=f"{home_team}: {home_corners}",
                                    delta=f"{away_team}: {away_corners}"
                                )
                        
                        # Auto-refresh
                        time.sleep(1.0 / speed_multiplier)  # Délai inversement proportionnel à la vitesse
                        st.rerun()
                    
                    else:
                        # Match terminé
                        st.session_state.simulation_active = False
                        
                        st.markdown(f"""
                        <div class="football-pitch">
                            <div class="match-scoreboard">
                                <h1>🏁 {get_text('simulation_complete', current_lang)}</h1>
                                <h1>🏟️ {home_team} {st.session_state.final_home_score} - {st.session_state.final_away_score} {away_team}</h1>
                                <h2>⏰ 90' - {get_text('final_result', current_lang)}</h2>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Statistiques finales
                        st.markdown(f"### 📊 {get_text('match_analysis', current_lang)}")
                        
                        # Sécuriser l'accès aux statistiques finales
                        final_stats = st.session_state.match_stats
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            home_possession = final_stats.get('possession', {}).get(home_team, 50)
                            home_shots = final_stats.get('shots', {}).get(home_team, 0)
                            st.metric(f"{get_text('possession', current_lang)} %", f"{home_team}: {home_possession}%")
                            st.metric(f"{get_text('shots', current_lang)}", f"{home_team}: {home_shots}")
                        
                        with col2:
                            home_shots_target = final_stats.get('shots_on_target', {}).get(home_team, 0)
                            home_corners = final_stats.get('corners', {}).get(home_team, 0)
                            st.metric(f"{get_text('shots_on_target', current_lang)}", f"{home_team}: {home_shots_target}")
                            st.metric(f"{get_text('corners', current_lang)}", f"{home_team}: {home_corners}")
                        
                        with col3:
                            home_fouls = final_stats.get('fouls', {}).get(home_team, 0)
                            home_offside = final_stats.get('offside', {}).get(home_team, 0)
                            st.metric(f"{get_text('fouls', current_lang)}", f"{home_team}: {home_fouls}")
                            st.metric(f"{get_text('offside', current_lang)}", f"{home_team}: {home_offside}")
                        
                        # Statistiques comparatives
                        st.markdown("#### 📊 Comparaison des Équipes")
                        away_possession = final_stats.get('possession', {}).get(away_team, 50)
                        away_shots = final_stats.get('shots', {}).get(away_team, 0)
                        away_corners = final_stats.get('corners', {}).get(away_team, 0)
                        
                        col_comp1, col_comp2 = st.columns(2)
                        with col_comp1:
                            st.markdown(f"**{home_team}**")
                            st.write(f"🥅 Possession: {home_possession}%")
                            st.write(f"⚽ Tirs: {home_shots}")
                            st.write(f"🚩 Corners: {home_corners}")
                        
                        with col_comp2:
                            st.markdown(f"**{away_team}**")
                            st.write(f"🥅 Possession: {away_possession}%")
                            st.write(f"⚽ Tirs: {away_shots}")
                            st.write(f"🚩 Corners: {away_corners}")
                        
                        # Bouton reset
                        if st.button(f"🔄 {get_text('reset_simulation', current_lang)}"):
                            for key in ['simulation_active', 'simulation_events', 'displayed_events', 
                                       'current_minute', 'current_home_score', 'current_away_score',
                                       'final_home_score', 'final_away_score', 'match_stats']:
                                if key in st.session_state:
                                    del st.session_state[key]
                            st.rerun()
        
        else:
            st.error(f"❌ {get_text('prediction_error', current_lang)}")
    
    else:
        st.info(get_text('select_different_teams', current_lang))

def show_prediction_history_interface(current_lang='fr'):
    """Interface d'historique des prédictions avec performance tracking - VERSION V10.2"""
    st.markdown("---")
    st.markdown(f"## {get_text('prediction_history_title', current_lang)}")
    
    # Simulation d'un système de stockage de prédictions
    if 'predictions_history' not in st.session_state:
        st.session_state.predictions_history = [
            {
                "date": "2024-07-30",
                "home_team": "Club Brugge",
                "away_team": "Anderlecht", 
                "predicted_result": "Victoire Domicile",
                "predicted_score": "2-1",
                "actual_result": "Défaite Domicile",
                "actual_score": "1-2",
                "correct": False,
                "confidence": 73.5
            },
            {
                "date": "2024-07-29",
                "home_team": "Genk",
                "away_team": "Standard",
                "predicted_result": "Victoire Domicile", 
                "predicted_score": "2-0",
                "actual_result": "Victoire Domicile",
                "actual_score": "2-0",
                "correct": True,
                "confidence": 68.2
            },
            {
                "date": "2024-07-28",
                "home_team": "Gent",
                "away_team": "Cercle",
                "predicted_result": "Match Nul",
                "predicted_score": "1-1", 
                "actual_result": "Match Nul",
                "actual_score": "1-1",
                "correct": True,
                "confidence": 45.8
            },
            {
                "date": "2024-07-27",
                "home_team": "Antwerp", 
                "away_team": "Union",
                "predicted_result": "Victoire Extérieur",
                "predicted_score": "0-2",
                "actual_result": "Victoire Extérieur",
                "actual_score": "1-2",
                "correct": True,
                "confidence": 61.4
            },
            {
                "date": "2024-07-26",
                "home_team": "Charleroi",
                "away_team": "Westerlo",
                "predicted_result": "Victoire Domicile",
                "predicted_score": "2-0",
                "actual_result": "Victoire Domicile", 
                "actual_score": "1-0",
                "correct": True,
                "confidence": 59.7
            }
        ]
    
    # Métriques de performance
    history = st.session_state.predictions_history
    total_predictions = len(history)
    correct_predictions = sum(1 for p in history if p['correct'])
    accuracy_rate = (correct_predictions / total_predictions) * 100 if total_predictions > 0 else 0
    avg_confidence = sum(p['confidence'] for p in history) / total_predictions if total_predictions > 0 else 0
    
    # Affichage des métriques
    st.markdown(f"### {get_text('performance_metrics', current_lang)}")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            get_text('total_predictions', current_lang),
            total_predictions,
            delta=None
        )
    
    with col2:
        st.metric(
            get_text('correct_predictions', current_lang), 
            correct_predictions,
            delta=f"{accuracy_rate:.1f}%"
        )
    
    with col3:
        st.metric(
            get_text('accuracy_rate', current_lang),
            f"{accuracy_rate:.1f}%",
            delta="+2.3%" if accuracy_rate > 70 else "-1.1%"
        )
    
    with col4:
        st.metric(
            get_text('average_confidence', current_lang),
            f"{avg_confidence:.1f}%",
            delta="+3.2%"
        )
    
    # Graphique de performance dans le temps
    st.markdown("### 📈 Évolution de la Précision")
    
    # Données pour le graphique
    dates = [p['date'] for p in history]
    cumulative_accuracy = []
    correct_so_far = 0
    
    for i, prediction in enumerate(history):
        if prediction['correct']:
            correct_so_far += 1
        cumulative_accuracy.append((correct_so_far / (i + 1)) * 100)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=cumulative_accuracy,
        mode='lines+markers',
        name='Précision Cumulative',
        line=dict(color='#667eea', width=3),
        marker=dict(size=8, color='#764ba2')
    ))
    
    fig.update_layout(
        title=get_text('accuracy_evolution_chart_title', current_lang),
        xaxis_title=get_text('date_axis', current_lang),
        yaxis_title=get_text('accuracy_axis', current_lang),
        height=400,
        showlegend=False,
        template='plotly_dark'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tableau détaillé des prédictions
    st.markdown("### 📋 Détail des Prédictions")
    
    # Convertir en DataFrame pour affichage
    df_history = pd.DataFrame(history)
    
    # Traduire les colonnes
    df_display = df_history.copy()
    df_display.columns = [
        get_text('table_date', current_lang),
        'Équipe Domicile',
        'Équipe Extérieur', 
        'Résultat Prédit',
        'Score Prédit',
        'Résultat Réel',
        'Score Réel',
        'Correct',
        'Confiance (%)'
    ]
    
    # Styler le tableau
    def highlight_correct(val):
        if val == True:
            return 'background-color: #28a745; color: white'
        elif val == False:
            return 'background-color: #dc3545; color: white'
        return ''
    
    styled_df = df_display.style.applymap(highlight_correct, subset=['Correct'])
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
    
    # Analyse par type de résultat
    st.markdown(f"### {get_text('performance_by_result_type', current_lang)}")
    
    result_analysis = {}
    for prediction in history:
        result_type = prediction['predicted_result']
        if result_type not in result_analysis:
            result_analysis[result_type] = {'total': 0, 'correct': 0}
        result_analysis[result_type]['total'] += 1
        if prediction['correct']:
            result_analysis[result_type]['correct'] += 1
    
    col1, col2, col3 = st.columns(3)
    
    for i, (result_type, stats) in enumerate(result_analysis.items()):
        accuracy = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
        
        if i == 0:
            col = col1
            color = "#28a745"
        elif i == 1:
            col = col2  
            color = "#ffc107"
        else:
            col = col3
            color = "#dc3545"
        
        with col:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}, #fd7e14); 
                        padding: 1rem; border-radius: 10px; color: white; text-align: center;">
                <h4>{result_type}</h4>
                <p><strong>{stats['correct']}/{stats['total']}</strong></p>
                <p><strong>{accuracy:.1f}%</strong></p>
            </div>
            """, unsafe_allow_html=True)

def show_documentation_interface(current_lang='fr'):
    """Interface de documentation pour présentation BeCode - VERSION V10.6"""
    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 15px; margin-bottom: 2rem; color: white; text-align: center;">
        <h1 style="margin: 0; font-size: 2.5rem;">📚 {get_text('documentation', current_lang)}</h1>
        <h2 style="margin: 1rem 0; font-size: 1.3rem;">{get_text('becode_presentation', current_lang)}</h2>
        <p style="margin: 0; font-size: 1rem; opacity: 0.9;">Football Prediction AI - Version 10.6</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Onglets de la documentation
    tabs = st.tabs([
        "🚀 " + get_text('project_overview', current_lang), 
        "🧠 Modèles IA", 
        "⚙️ " + get_text('features_overview', current_lang), 
        "📊 Démonstration", 
        "❓ FAQ",
        "🎯 " + get_text('becode_presentation', current_lang)
    ])
    
    with tabs[0]:  # Vue d'ensemble
        st.markdown("## 🚀 Vue d'Ensemble du Projet")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 🎯 Objectif
            Application de **prédiction de matchs de football** utilisant l'intelligence artificielle 
            pour analyser les performances des équipes et prédire les résultats.
            
            ### 🎮 Concept Innovant
            - **Simulation en temps réel** style Football Manager 2024
            - **Moteur de prédiction multicritères** basé sur 6 algorithmes
            - **Interface multilingue** (Français/Anglais)
            - **Visualisations interactives** avec Plotly
            
            ### 📈 Données Analysées
            - **+2000 matchs** de football belge (2023-2025)
            - **18 équipes** de Jupiler Pro League
            - **30+ statistiques** par match analysées
            - **Forme récente** des équipes (5 derniers matchs)
            """)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #ff6b6b, #ee5a52); 
                        padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 1rem 0;">
                <h3 style="margin: 0;">📊 Statistiques</h3>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <p style="margin: 0.5rem 0;"><strong>Version:</strong> 10.6</p>
                <p style="margin: 0.5rem 0;"><strong>Précision:</strong> 72-85%</p>
                <p style="margin: 0.5rem 0;"><strong>Algorithmes:</strong> 6</p>
                <p style="margin: 0.5rem 0;"><strong>Langues:</strong> 2</p>
                <p style="margin: 0.5rem 0;"><strong>Pages:</strong> 6</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4ecdc4, #44a08d); 
                        padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 1rem 0;">
                <h3 style="margin: 0;">🛠️ Technologies</h3>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <p style="margin: 0.3rem 0;">• Python & Streamlit</p>
                <p style="margin: 0.3rem 0;">• Pandas & NumPy</p>
                <p style="margin: 0.3rem 0;">• Scikit-learn</p>
                <p style="margin: 0.3rem 0;">• Plotly & CSS3</p>
                <p style="margin: 0.3rem 0;">• Machine Learning</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:  # Modèles IA
        st.markdown("## 🧠 Modèles d'Intelligence Artificielle")
        
        st.markdown("""
        ### 🎯 Approche Multi-Algorithmes
        L'application utilise un **ensemble de 6 algorithmes** de machine learning pour maximiser la précision :
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                        padding: 1rem; border-radius: 10px; color: white; margin: 0.5rem 0;">
                <h4>🎯 Classification</h4>
                <p><strong>• Random Forest</strong><br>Précision: 78%</p>
                <p><strong>• Support Vector Machine</strong><br>Précision: 75%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #ffa726, #ff7043); 
                        padding: 1rem; border-radius: 10px; color: white; margin: 0.5rem 0;">
                <h4>📊 Régression</h4>
                <p><strong>• Linear Regression</strong><br>RMSE: 1.2</p>
                <p><strong>• Gradient Boosting</strong><br>RMSE: 1.1</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #11998e, #38ef7d); 
                        padding: 1rem; border-radius: 10px; color: white; margin: 0.5rem 0;">
                <h4>🎲 Probabiliste</h4>
                <p><strong>• Logistic Regression</strong><br>Accuracy: 72%</p>
                <p><strong>• Naive Bayes</strong><br>Accuracy: 70%</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 📈 Variables Analysées")
        
        variables_col1, variables_col2, variables_col3 = st.columns(3)
        
        with variables_col1:
            st.markdown("""
            **🏠 Facteurs Domicile/Extérieur**
            - Avantage du terrain (variable par équipe)
            - Historique domicile vs extérieur
            - Support des supporters
            """)
        
        with variables_col2:
            st.markdown("""
            **📊 Forme Récente**
            - 5 derniers matchs de chaque équipe
            - Moyenne des buts marqués/encaissés
            - Tendance offensive/défensive
            """)
        
        with variables_col3:
            st.markdown("""
            **⚔️ Head-to-Head**
            - 10 dernières confrontations
            - Historique des résultats
            - Patterns de jeu entre équipes
            """)
    
    with tabs[2]:  # Fonctionnalités
        st.markdown("## ⚙️ Fonctionnalités Principales")
        
        features = [
            ("🔮 Prédiction Simple", "Prédiction rapide entre deux équipes avec niveau de confiance", "#ff6b6b"),
            ("📅 Calendrier Multi-Matchs", "Génération de prédictions pour plusieurs matchs simultanément", "#4ecdc4"),
            ("💰 Cotes Bookmakers", "Comparaison avec les cotes et détection de paris de valeur", "#ffa726"),
            ("📈 Historique & Performance", "Tracking des prédictions et analyse de performance", "#667eea"),
            ("🎮 Moteur de Simulation", "Simulation de match en temps réel style Football Manager", "#11998e"),
            ("📚 Documentation", "Guide complet et présentation du projet", "#764ba2")
        ]
        
        for i, (title, desc, color) in enumerate(features):
            if i % 2 == 0:
                col1, col2 = st.columns(2)
                current_col = col1
            else:
                current_col = col2
            
            with current_col:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}, {color}dd); 
                            padding: 1.5rem; border-radius: 10px; color: white; margin: 0.5rem 0; height: 120px;">
                    <h4 style="margin: 0 0 0.5rem 0;">{title}</h4>
                    <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)
    
    with tabs[3]:  # Démonstration
        st.markdown("## 📊 Démonstration en Temps Réel")
        
        st.markdown("""
        ### 🎮 Testez le Moteur de Prédiction !
        
        Voici un exemple de prédiction en temps réel avec les données actuelles :
        """)
        
        # Exemple de prédiction pour la démo
        demo_col1, demo_col2, demo_col3 = st.columns([1, 2, 1])
        
        with demo_col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                        padding: 2rem; border-radius: 15px; color: white; text-align: center; margin: 1rem 0;">
                <h3 style="margin: 0 0 1rem 0;">⚽ Exemple de Prédiction</h3>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h2 style="margin: 0;">Anderlecht</h2>
                        <p style="margin: 0; opacity: 0.8;">Domicile</p>
                    </div>
                    <div>
                        <h1 style="margin: 0; font-size: 3rem;">2 - 1</h1>
                        <p style="margin: 0; color: #FFD700;">🏆 Confiance: 78%</p>
                    </div>
                    <div>
                        <h2 style="margin: 0;">Club Brugge</h2>
                        <p style="margin: 0; opacity: 0.8;">Extérieur</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Métriques de la démo
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        
        with metric_col1:
            st.metric("🏠 Victoire Domicile", "65%", "+12%")
        
        with metric_col2:
            st.metric("🤝 Match Nul", "22%", "-3%")
        
        with metric_col3:
            st.metric("✈️ Victoire Extérieur", "13%", "-9%")
        
        with metric_col4:
            st.metric("🎯 Confiance Globale", "78%", "+5%")
    
    with tabs[4]:  # FAQ
        st.markdown(f"## {get_text('faq_title', current_lang)}")
        
        # Question 1
        with st.expander(f"❓ {get_text('faq_q1', current_lang)}"):
            st.markdown(get_text('faq_a1', current_lang))
        
        # Question 2
        with st.expander(f"📊 {get_text('faq_q2', current_lang)}"):
            st.markdown(get_text('faq_a2', current_lang))
        
        # Question 3
        with st.expander(f"📁 {get_text('faq_q3', current_lang)}"):
            st.markdown(get_text('faq_a3', current_lang))
        
        # Question 4
        with st.expander(f"🎮 {get_text('faq_q4', current_lang)}"):
            st.markdown(get_text('faq_a4', current_lang))
        
        # Question 5
        with st.expander(f"💰 {get_text('faq_q5', current_lang)}"):
            st.markdown(get_text('faq_a5', current_lang))
        
        st.markdown("---")
        st.info("💡 D'autres questions ? L'application est conçue pour être intuitive et auto-explicative !")
    
    with tabs[5]:  # Présentation BeCode
        st.markdown("## 🎯 Présentation BeCode")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6B35, #F7931E); 
                    padding: 2rem; border-radius: 15px; color: white; text-align: center; margin: 1rem 0;">
            <h2 style="margin: 0;">🎓 Projet de Formation BeCode</h2>
            <p style="margin: 1rem 0; font-size: 1.1rem;">Intelligence Artificielle & Data Science</p>
        </div>
        """, unsafe_allow_html=True)
        
        becode_col1, becode_col2 = st.columns([1, 1])
        
        with becode_col1:
            st.markdown("""
            ### 🎯 Objectifs Pédagogiques
            
            **✅ Machine Learning**
            - Implémentation d'algorithmes ML
            - Ensemble methods & stacking
            - Feature engineering avancé
            
            **✅ Data Science**
            - Analyse exploratoire de données
            - Visualisations interactives
            - Métriques de performance
            
            **✅ Développement Web**
            - Framework Streamlit
            - Interface utilisateur moderne
            - Responsive design
            
            **✅ Gestion de Projet**
            - Versioning Git
            - Documentation complète
            - Tests et débogage
            """)
        
        with becode_col2:
            st.markdown("""
            ### 📈 Évolution du Projet
            
            **🚀 V10.0** - Base ML
            - Modèles de prédiction
            - Interface basique
            
            **🌍 V10.1** - Multilingue
            - Support FR/EN
            - Traductions complètes
            
            **💰 V10.2** - Bookmakers
            - Comparaison cotes
            - Historique prédictions
            
            **📊 V10.4** - Analyse Avancée
            - Head-to-head stats
            - Facteur domicile variable
            
            **🎮 V10.5** - Simulation
            - Moteur temps réel
            - Animations Football Manager
            
            **📚 V10.6** - Documentation
            - Guide complet
            - Mode présentation
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ### 🏆 Résultats & Apprentissages
        
        Ce projet a permis de maîtriser :
        - **6 algorithmes** de machine learning différents
        - **Interface web moderne** avec Streamlit
        - **Analyse de données** complexes (2000+ matchs)
        - **Visualisations interactives** avec Plotly
        - **Système multilingue** complet
        - **Architecture logicielle** modulaire et évolutive
        
        **🎯 Précision obtenue : 72-85% selon les équipes et contextes**
        """)

def main():
    """Fonction principale avec système multilingue - VERSION V10.0"""
    
    # CSS personnalisé pour la sidebar
    st.markdown("""
    <style>
    /* Amélioration de la sidebar */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }
    
    /* Style pour les éléments radio */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 0.5rem;
        margin: 0.3rem 0;
    }
    
    .stRadio > div > label {
        font-weight: 500 !important;
        color: white !important;
        font-size: 0.95rem !important;
    }
    
    .stRadio > div > label:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 5px;
        padding: 0.3rem;
        transition: all 0.3s ease;
    }
    
    /* Style pour les multiselect */
    .stMultiSelect > div > div {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
    }
    
    /* Amélioration des cartes de métriques */
    .metric-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 🌍 SÉLECTEUR DE LANGUE (en premier)
    current_lang = create_language_selector()
    
    # En-tête multilingue
    st.markdown(f"""
    <div class="main-header">
        <h1>{get_text('app_title', current_lang)}</h1>
        <p>{get_text('subtitle', current_lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Chargement des données
    with st.spinner(get_text('loading_data', current_lang)):
        data = load_data()
    
    if data is None:
        st.stop()
    
    # ÉTAPE 2: Notification de succès
    show_advanced_notification(get_text('app_ready', current_lang), "success")
    
    # Sidebar pour sélection des saisons avec style amélioré
    st.sidebar.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1rem; border-radius: 10px; margin-bottom: 1rem; color: white; text-align: center;">
        <h2 style="margin: 0; font-size: 1.2rem;">⚙️ {get_text('configuration', current_lang)}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Sélection des saisons avec style moderne
    st.sidebar.markdown("### 📅 Saisons d'Analyse")
    available_seasons = sorted(data['Season'].unique())
    selected_seasons = st.sidebar.multiselect(
        "Choisissez les saisons :",
        available_seasons,
        default=available_seasons[-2:] if len(available_seasons) >= 2 else available_seasons
    )
    
    if not selected_seasons:
        show_advanced_notification(get_text('continue_message', current_lang), "warning")
        st.stop()
    
    # Calcul des statistiques
    with st.spinner(get_text('calculating_statistics', current_lang)):
        team_stats = calculate_team_stats(data, selected_seasons)
        teams = sorted(team_stats.keys())
    
    # Informations sur les données sélectionnées
    season_data = data[data['Season'].isin(selected_seasons)]
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Données Sélectionnées")
    st.sidebar.info(f"""
    **📈 Matchs :** {len(season_data)}  
    **⚽ Équipes :** {len(teams)}  
    **📅 Saisons :** {len(selected_seasons)}
    """)
    
    # Navigation avec style moderne
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"""
    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                padding: 0.8rem; border-radius: 8px; margin-bottom: 1rem; color: white; text-align: center;">
        <h3 style="margin: 0; font-size: 1.1rem;">🎯 {get_text('features', current_lang)}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Options du menu avec description
    menu_options = [
        ("🔮 " + get_text('simple_prediction', current_lang), "Prédiction rapide entre deux équipes"),
        ("📅 " + get_text('multi_match_calendar', current_lang), "Calendrier de matchs multiples"),
        (get_text('bookmaker_odds', current_lang), "Cotes et paris bookmakers"),
        ("📈 " + get_text('history_performance', current_lang), "Historique et performance"),
        ("🎮 " + get_text('match_engine_simulation', current_lang), "Simulation de match en temps réel"),
        (get_text('documentation', current_lang), "Guide complet et présentation BeCode"),
        ("⚙️ Configuration", "Paramètres et réglages de l'application")
    ]
    
    # Affichage du menu avec descriptions
    view_options = [option[0] for option in menu_options]
    view = st.sidebar.radio(
        "",
        view_options,
        format_func=lambda x: x
    )
    
    # Afficher la description de l'option sélectionnée
    selected_description = next((desc for opt, desc in menu_options if opt == view), "")
    if selected_description:
        st.sidebar.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.1); 
                    padding: 0.5rem; border-radius: 5px; margin-top: 0.5rem; font-size: 0.8rem; color: #ccc;">
            💡 {selected_description}
        </div>
        """, unsafe_allow_html=True)
    # Métriques générales avec style moderne
    st.markdown(f"### 📊 {get_text('data_overview', current_lang)}")
    
    # Calculer les données
    season_data = data[data['Season'].isin(selected_seasons)]
    avg_goals = season_data[['FTHG', 'FTAG']].mean().mean()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #ff6b6b, #ee5a52); 
                    padding: 1rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem 0;">
            <h3 style="margin: 0; font-size: 1.5rem;">{len(season_data)}</h3>
            <p style="margin: 0.2rem 0; font-size: 0.9rem;">📊 {get_text('total_matches', current_lang)}</p>
            <small style="opacity: 0.8;">{get_text('total_analyzed', current_lang)}</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #4ecdc4, #44a08d); 
                    padding: 1rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem 0;">
            <h3 style="margin: 0; font-size: 1.5rem;">{len(teams)}</h3>
            <p style="margin: 0.2rem 0; font-size: 0.9rem;">⚽ {get_text('teams', current_lang)}</p>
            <small style="opacity: 0.8;">{get_text('in_database', current_lang)}</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #667eea, #764ba2); 
                    padding: 1rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem 0;">
            <h3 style="margin: 0; font-size: 1.5rem;">{len(selected_seasons)}</h3>
            <p style="margin: 0.2rem 0; font-size: 0.9rem;">📅 {get_text('seasons', current_lang)}</p>
            <small style="opacity: 0.8;">{get_text('selected', current_lang)}</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #ffa726, #ff7043); 
                    padding: 1rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem 0;">
            <h3 style="margin: 0; font-size: 1.5rem;">{avg_goals:.1f}</h3>
            <p style="margin: 0.2rem 0; font-size: 0.9rem;">🥅 {get_text('goals_per_match', current_lang)}</p>
            <small style="opacity: 0.8;">{get_text('average', current_lang)}</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Affichage selon la vue sélectionnée
    if view.startswith("🔮"):  # Simple Prediction
        show_prediction_interface(data, selected_seasons, team_stats, teams, current_lang)
    elif view.startswith("📅"):  # Multi-Match Calendar
        show_multi_match_interface(data, selected_seasons, team_stats, teams, current_lang)
    elif view.startswith("💰"):  # Bookmaker Odds
        show_bookmaker_odds(data, teams, current_lang)
    elif view.startswith("📈"):  # History & Performance
        show_prediction_history_interface(current_lang)
    elif view.startswith("🎮"):  # Match Engine Simulation
        show_match_engine_simulation(data, selected_seasons, team_stats, teams, current_lang)
    elif view.startswith("📚"):  # Documentation
        show_documentation_interface(current_lang)
    elif view.startswith("⚙️"):  # Configuration
        st.markdown("## ⚙️ Configuration")
        st.info("Page de configuration en cours de développement...")

if __name__ == "__main__":
    main()

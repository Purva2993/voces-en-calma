"""
Bilingual Support Module - English/Spanish
Provides translations for all UI text
"""

TRANSLATIONS = {
    'en': {
        # Navigation
        'app_title': 'Voces Digital App',
        'home': 'Home',
        'share_story': 'Share Story',
        'healers': 'Our Healers',
        'insights': 'Insights',
        
        # Home page
        'main_header': '🕊️ Voces en Calma',
        'subtitle': 'Your story matters. Your healing matters.',
        'welcome_text': '''Welcome to a quiet digital room where you can share how stress shows up in your life—
        anonymously, safely, and without judgment.<br><br>
        Here, your words help Latina wellness practitioners who blend ancestral healing 
        (curanderismo, prayer, somatic rituals) with modern therapeutic approaches 
        understand what our community truly needs.<br><br>
        <strong>You are not alone. We are listening.</strong>''',
        'community_impact': 'Community Impact',
        'stories_shared': 'stories shared, voices heard',
        'private': 'Private',
        'private_desc': 'No names, no emails, no tracking. Your story stays anonymous.',
        'supported': 'Supported',
        'supported_desc': 'Connect with healing practices that feel right for you.',
        'community_led': 'Community-Led',
        'community_led_desc': 'Latina practitioners creating space for our collective healing.',
        'how_it_works': 'How It Works',
        'step1': '**1. Share Your Story** 📝',
        'step1_desc': 'In just a few words, describe how stress is showing up in your life this week.',
        'step2': '**2. Choose Your Support** 💫',
        'step2_desc': 'Tell us what kinds of healing practices you\'re open to exploring.',
        'step3': '**3. We Listen & Respond** 👂',
        'step3_desc': 'Latina wellness practitioners use these insights to create offerings that meet real community needs.',
        'ready_to_share': '👈 **Ready to share your story?** Click \'Share Story\' in the sidebar to begin.',
        'about': 'About Voces en Calma',
        'about_text': '''This platform was created to honor the wisdom of our ancestors while embracing modern understanding of trauma, stress, and healing.

We believe healing happens in community, and that the remedies our abuelas taught us—prayer, herbs, touch, music, gathering—are just as powerful when combined with contemporary therapeutic tools.

This is a space where both matter. Where you matter.''',
        'footer': '💚 Made with love for our community<br>Questions? Feedback? Use the sidebar menu to explore or contact us.',
        
        # Share Story page
        'share_story_title': '📝 Share Your Story',
        'share_story_subtitle': 'Your voice matters. Your experience matters.',
        'privacy_header': '🔒 Privacy & Anonymity (Please Read)',
        'tell_us_story': 'Tell Us Your Story',
        'story_prompt': '*In your own words, describe how stress is showing up in your life this week.*',
        'story_placeholder': 'Example: This week I feel overwhelmed by family expectations. I love my family but sometimes I feel like I\'m losing myself trying to make everyone happy...',
        'character_count_min': '✍️ {count}/700 characters (minimum 20)',
        'character_count_close': '⚠️ {count}/700 characters (getting close to limit)',
        'character_count_ok': '✅ {count}/700 characters',
        'support_types': 'What Kind of Support Are You Open To?',
        'support_desc': '*Select all that feel right for you. There\'s no wrong answer.*',
        'anything_else': 'Anything Else? (Optional)',
        'practitioner_note': 'How do you want practitioners to show up for you?',
        'practitioner_placeholder': 'Example: I need something gentle and not too structured...',
        'consent_text': 'I understand that my anonymous story will be read by Latina wellness practitioners to help shape community support offerings.',
        'submit_button': '🕊️ Share My Story',
        'story_heard': '✨ Your Story Has Been Heard',
        'detected_emotion': 'We sense you may be feeling: {emotion}',
        'thank_you': '''Thank you for trusting us with your experience.
        
        Your words are now part of our community\'s collective voice, helping Latina wellness 
        practitioners understand what we need most.
        
        What happens next?
        - Practitioners will review anonymous insights (not individual stories)
        - New support offerings will be shaped based on what the community is asking for
        - You can return anytime to share again
        
        You are not alone in this journey. 💚''',
        'back_home': '← Back to Home',
        'share_another': 'Share Another Story',
        
        # Support options
        'journaling': 'Journaling prompts',
        'group_circles': 'Virtual group circles',
        'one_on_one': 'One-on-one coaching',
        'art_therapy': 'Art/creative therapy',
        'bodywork': 'Massage/bodywork',
        'spiritual': 'Spiritual/faith-rooted support',
        'self_study': 'Quiet self-study resources',
        'somatic': 'Movement/somatic practices',
        'herbal': 'Herbal remedies & traditional healing',
        
        # Emotions
        'anxiety': '😰 Anxiety/Worry',
        'sadness': '😢 Sadness',
        'exhaustion': '😴 Exhaustion/Burnout',
        'guilt': '😔 Guilt/Shame',
        'anger': '😤 Anger/Frustration',
        'hope': '🌟 Hope/Positivity',
        'overwhelm': '🌊 Overwhelm',
        'family_stress': '👨‍👩‍👧‍👦 Family Stress',
        'neutral': '😌 Neutral',
        
        # Dashboard
        'dashboard_title': '📊 Community Insights Dashboard',
        'dashboard_subtitle': 'Understanding what our community needs',
        'community_stories': 'Community Stories',
        'external_sources': 'External Sources',
        'top_emotion': 'Top Community Emotion',
        'emotional_landscape': '🎭 Emotional Landscape of Our Community',
        'emotional_landscape_desc': '*What emotions are surfacing most in our community?*',
        'community_vs_broader': '🌍 Community Voice vs Broader Conversations',
        'comparison_desc': '*How do our community emotions compare to broader Latina wellness discussions?*',
        'key_insights': '💡 Key Insights',
        'opportunities': '🔍 Opportunities',
        'themes_title': '📚 Themes in Broader Latina Wellness Conversations',
        'themes_desc': '*What topics are being discussed in public Latina wellness spaces?*',
        'support_preferences': '🤝 Support Preferences',
        'support_preferences_desc': '*What types of support is the community asking for?*',
        'emotion_support_matching': '🔗 Emotion-Support Matching',
        'emotion_support_desc': '*Which emotions are paired with which support requests?*',
        'recent_voices': '📝 Recent Community Voices',
        'recent_voices_desc': '*Anonymous story excerpts to understand community needs*',
        'external_conversations': '🌐 Sample External Conversations',
        'external_conversations_desc': '*Recent discussions from Latina wellness blogs, forums, and communities*',
        
        # Healers page
        'healers_title': '🌺 Our Circle of Healers',
        'healers_subtitle': 'Meet the Latina wellness practitioners holding space for our community',
        'healers_intro': '''These practitioners blend the wisdom of our ancestors with modern therapeutic approaches.
They honor *curanderismo*, prayer circles, herbal remedies, and somatic rituals while 
integrating trauma-informed coaching, mindfulness, and psychoeducation.

**This platform is their listening tool** - helping them understand what you need so they 
can create offerings that truly serve our community.''',
        'healing_philosophy': 'Our Healing Philosophy',
        'ancestral_wisdom': '🌿 Ancestral Wisdom',
        'modern_approaches': '🧠 Modern Approaches',
        'how_this_works': '💡 How This Works',
        'how_this_works_text': '''**💡 How This Works:**

These practitioners use insights from anonymous community stories (not individual details) 
to understand what support is needed most. Based on these patterns, they create:

- Group healing circles
- Workshops & classes  
- One-on-one sessions
- Self-guided resources
- Community events

**Your voice shapes what we offer.** When you share your story, you help us create 
the exact kinds of support our community is asking for.''',
        'ready_share_story': '🕊️ Ready to Share Your Story?',
        
        # Insights Dashboard - Additional translations
        'export_data': '📥 Export Data & Reports',
        'export_desc': '*Download insights and reports for your records*',
        'stories_csv': '📊 Stories CSV',
        'emotions_csv': '😊 Emotions CSV',
        'support_csv': '🤝 Support CSV',
        'external_csv': '🌐 External CSV',
        'comprehensive_report': '📄 Comprehensive Report',
        'report_desc': '📝 Generate a comprehensive text report with all key insights, comparisons, and statistics',
        'download_report': '📄 Download Report',
        'key_emotion_insights': '📊 Key Emotion Insights',
        'stories': 'stories',
        'of_total': 'of total',
        'more_prominent': '**More prominent in our community:**',
        'higher': 'higher',
        'gaining_traction': '**Topics gaining traction externally:**',
        'consider_offerings': 'Consider creating offerings',
        'theme_insights': '💡 **Theme Insights:** The most discussed theme in broader conversations is',
        'align_differ': 'Consider how our community\'s needs align with or differ from these broader conversations.',
        'show_stories_from': 'Show stories from:',
        'last_7_days': 'Last 7 days',
        'last_30_days': 'Last 30 days',
        'all_time': 'All time',
        'total_stories_period': 'total stories in this time period',
        'full_story': '**Full Story:**',
        'additional_context': '**Additional Context:**',
        'details': '**Details:**',
        'date': '**Date:**',
        'detected_emotion_label': '**Emotion:**',
        'confidence': 'Confidence:',
        'support_requested': '**Support Requested:**',
        'theme': 'Theme:',
        'analysis': '**Analysis:**',
        'page': 'Page',
        'of': 'of',
        'first': '⏮️ First',
        'previous': '⬅️ Previous',
        'next': 'Next ➡️',
        'last': 'Last ⏭️',
        'key_patterns': '💡 Key Patterns',
        'common_themes': 'Common Themes Mentioned',
        'mentioned_times': 'mentioned {count} times',
        'support_gaps': 'Support Gaps to Consider',
        'analyze_themes': '🔍 Analyze if high-frequency themes have corresponding support options.',
        'consider_offerings_repeated': '💡 Consider creating offerings that specifically address repeated concerns.',
        'suggested_actions': '🎯 Suggested Actions',
        'high_demand': '**High Demand**:',
        'is_most_requested': 'is most requested',
        'times': 'times',
        'consider_expanding': 'Consider expanding offerings in this area.',
        'low_awareness': '**Low Awareness**: Some support types are rarely selected. Consider educating community about these options.',
        'active_community': '**Active Community**:',
        'stories_this_week': 'stories this week shows strong engagement. Great time to launch new offerings!',
        'promote_platform': 'Start by promoting the platform to your community. Share the link to encourage story submissions.',
        'footer_privacy': '💚 This dashboard respects complete anonymity - no personal identifiers are ever stored<br>Data shown here represents aggregate community needs, not individual details',
        'logout': '🔓 Logout',
        
        # More Insights translations
        'emotion_distribution_title': 'Emotion Distribution in Community Stories',
        'num_stories_axis': 'Number of Stories',
        'comparison_title': 'Emotion Comparison: Our Community vs Broader Latina Wellness Conversations',
        'percentage_axis': 'Percentage (%)',
        'our_community': 'Our Community',
        'broader_discussions': 'Broader Discussions',
        'theme_distribution_title': 'Theme Distribution in External Content',
        'requested_support_types': 'Requested Support Types',
        'count': 'Count',
        'emotion_support_heatmap': 'Emotion-Support Correlation Heatmap',
        'support_type': 'Support Type',
        'emotion': 'Emotion',
        'heatmap_help': '💡 **How to read this:** Numbers show how many times each emotion paired with each support type. Higher numbers (darker blue) indicate stronger connections.',
        'need_stories_comparison': 'Need both community stories and external data for comparison.',
        'need_stories_heatmap': 'Need at least 3 stories to show emotion-support patterns.',
        'need_emotion_tags': 'Need more stories with emotion tags to generate correlation analysis.',
        'no_stories_period': 'No stories found for this time period.',
        'view_breakdown': '📋 View Detailed Breakdown',
        'blog': 'blog',
        'forum': 'forum',
        'reddit': 'reddit',
        
        # Trend Analysis
        'trend_analysis': '📈 Emotion Trends Over Time',
        'trend_analysis_desc': '*Track how community emotions evolve week by week*',
        'select_emotions': 'Select emotions to track:',
        'all_emotions': 'All Emotions',
        'week': 'Week',
        'emotion_trends_title': 'Community Emotion Trends',
        'need_data_trends': 'Need at least 2 weeks of data to show trends.',
        
        # Advanced Filtering
        'advanced_filters': '🔍 Advanced Filters',
        'filter_by_emotion': 'Filter by Emotion:',
        'filter_by_support': 'Filter by Support Type:',
        'filter_by_date': 'Filter by Date Range:',
        'all': 'All',
        'apply_filters': 'Apply Filters',
        'clear_filters': 'Clear Filters',
        'filtered_results': 'Filtered Results:',
        'matching_stories': 'matching stories',
        
        # Contact section
        'contact_us': 'Contact Us',
        'get_in_touch': 'Get in Touch',
        'get_in_touch_text': "We're here to support you and answer any questions.",
        'email': 'Email:',
        'phone': 'Phone:',
        'hours': 'Hours:',
        'need_support': 'Need Support?',
        'need_support_list': '''- Questions about the platform
- Technical assistance
- Practitioner inquiries
- Partnership opportunities
- General wellness resources

*We typically respond within 24 hours.*''',
        'community_guidelines': 'Community Guidelines',
        'be_respectful': 'Be Respectful',
        'be_respectful_text': "Honor each person's journey and experience with compassion.",
        'stay_anonymous': 'Stay Anonymous',
        'stay_anonymous_text': 'Protect your privacy and the privacy of others.',
        'seek_support': 'Seek Support',
        'seek_support_text': 'This platform connects you with healing resources.',
    },
    'es': {
        # Navegación
        'app_title': 'Aplicación Digital Voces',
        'home': 'Inicio',
        'share_story': 'Compartir Historia',
        'healers': 'Nuestras Sanadoras',
        'insights': 'Perspectivas',
        
        # Página principal
        'main_header': '🕊️ Voces en Calma',
        'subtitle': 'Tu historia importa. Tu sanación importa.',
        'welcome_text': '''Bienvenida a un espacio digital tranquilo donde puedes compartir cómo el estrés se manifiesta en tu vida—
        de forma anónima, segura y sin juicio.<br><br>
        Aquí, tus palabras ayudan a las practicantes de bienestar Latinas que combinan sanación ancestral 
        (curanderismo, oración, rituales somáticos) con enfoques terapéuticos modernos 
        a entender lo que nuestra comunidad realmente necesita.<br><br>
        <strong>No estás sola. Estamos escuchando.</strong>''',
        'community_impact': 'Impacto Comunitario',
        'stories_shared': 'historias compartidas, voces escuchadas',
        'private': 'Privado',
        'private_desc': 'Sin nombres, correos ni rastreo. Tu historia permanece anónima.',
        'supported': 'Apoyada',
        'supported_desc': 'Conéctate con prácticas de sanación que te hagan sentir bien.',
        'community_led': 'Liderado por la Comunidad',
        'community_led_desc': 'Practicantes Latinas creando espacio para nuestra sanación colectiva.',
        'how_it_works': 'Cómo Funciona',
        'step1': '**1. Comparte Tu Historia** 📝',
        'step1_desc': 'En pocas palabras, describe cómo el estrés se está manifestando en tu vida esta semana.',
        'step2': '**2. Elige Tu Apoyo** 💫',
        'step2_desc': 'Dinos qué tipos de prácticas de sanación estás dispuesta a explorar.',
        'step3': '**3. Escuchamos y Respondemos** 👂',
        'step3_desc': 'Las practicantes de bienestar Latinas usan estas perspectivas para crear ofertas que satisfagan las necesidades reales de la comunidad.',
        'ready_to_share': '👈 **¿Lista para compartir tu historia?** Haz clic en \'Compartir Historia\' en la barra lateral para comenzar.',
        'about': 'Sobre Voces en Calma',
        'about_text': '''Esta plataforma fue creada para honrar la sabiduría de nuestras ancestras mientras abrazamos la comprensión moderna del trauma, el estrés y la sanación.

Creemos que la sanación ocurre en comunidad, y que los remedios que nuestras abuelas nos enseñaron—la oración, las hierbas, el tacto, la música, la reunión—son igual de poderosos cuando se combinan con herramientas terapéuticas contemporáneas.

Este es un espacio donde ambos importan. Donde tú importas.''',
        'footer': '💚 Hecho con amor para nuestra comunidad<br>¿Preguntas? ¿Comentarios? Usa el menú lateral para explorar o contáctanos.',
        
        # Página de compartir historia
        'share_story_title': '📝 Comparte Tu Historia',
        'share_story_subtitle': 'Tu voz importa. Tu experiencia importa.',
        'privacy_header': '🔒 Privacidad y Anonimato (Por Favor Lee)',
        'tell_us_story': 'Cuéntanos Tu Historia',
        'story_prompt': '*En tus propias palabras, describe cómo el estrés se está manifestando en tu vida esta semana.*',
        'story_placeholder': 'Ejemplo: Esta semana me siento abrumada por las expectativas familiares. Amo a mi familia pero a veces siento que me estoy perdiendo a mí misma tratando de hacer felices a todos...',
        'character_count_min': '✍️ {count}/700 caracteres (mínimo 20)',
        'character_count_close': '⚠️ {count}/700 caracteres (cerca del límite)',
        'character_count_ok': '✅ {count}/700 caracteres',
        'support_types': '¿Qué Tipo de Apoyo Te Interesa?',
        'support_desc': '*Selecciona todas las que te parezcan adecuadas. No hay respuesta incorrecta.*',
        'anything_else': '¿Algo Más? (Opcional)',
        'practitioner_note': '¿Cómo quieres que las practicantes te apoyen?',
        'practitioner_placeholder': 'Ejemplo: Necesito algo gentil y no muy estructurado...',
        'consent_text': 'Entiendo que mi historia anónima será leída por practicantes de bienestar Latinas para ayudar a crear ofertas de apoyo comunitario.',
        'submit_button': '🕊️ Compartir Mi Historia',
        'story_heard': '✨ Tu Historia Ha Sido Escuchada',
        'detected_emotion': 'Sentimos que puedes estar sintiendo: {emotion}',
        'thank_you': '''Gracias por confiar en nosotras con tu experiencia.
        
        Tus palabras ahora son parte de la voz colectiva de nuestra comunidad, ayudando a las practicantes 
        de bienestar Latinas a entender lo que más necesitamos.
        
        **¿Qué sigue?**
        - Las practicantes revisarán perspectivas anónimas (no historias individuales)
        - Nuevas ofertas de apoyo se crearán basadas en lo que la comunidad está pidiendo
        - Puedes regresar en cualquier momento para compartir de nuevo
        
        **No estás sola en este viaje. 💚**''',
        'back_home': '← Volver al Inicio',
        'share_another': 'Compartir Otra Historia',
        
        # Opciones de apoyo
        'journaling': 'Indicaciones para escribir diario',
        'group_circles': 'Círculos grupales virtuales',
        'one_on_one': 'Asesoramiento individual',
        'art_therapy': 'Arte/terapia creativa',
        'bodywork': 'Masajes/trabajo corporal',
        'spiritual': 'Apoyo espiritual/basado en fe',
        'self_study': 'Recursos de autoestudio tranquilo',
        'somatic': 'Movimiento/prácticas somáticas',
        'herbal': 'Remedios herbales y sanación tradicional',
        
        # Emociones
        'anxiety': '😰 Ansiedad/Preocupación',
        'sadness': '😢 Tristeza',
        'exhaustion': '😴 Agotamiento/Burnout',
        'guilt': '😔 Culpa/Vergüenza',
        'anger': '😤 Enojo/Frustración',
        'hope': '🌟 Esperanza/Positividad',
        'overwhelm': '🌊 Abrumada',
        'family_stress': '👨‍👩‍👧‍👦 Estrés Familiar',
        'neutral': '😌 Neutral',
        
        # Panel de control
        'dashboard_title': '📊 Panel de Perspectivas Comunitarias',
        'dashboard_subtitle': 'Entendiendo lo que nuestra comunidad necesita',
        'community_stories': 'Historias Comunitarias',
        'external_sources': 'Fuentes Externas',
        'top_emotion': 'Emoción Principal de la Comunidad',
        'emotional_landscape': '🎭 Panorama Emocional de Nuestra Comunidad',
        'emotional_landscape_desc': '*¿Qué emociones están surgiendo más en nuestra comunidad?*',
        'community_vs_broader': '🌍 Voz Comunitaria vs Conversaciones Más Amplias',
        'comparison_desc': '*¿Cómo se comparan las emociones de nuestra comunidad con las discusiones más amplias de bienestar Latina?*',
        'key_insights': '💡 Perspectivas Clave',
        'opportunities': '🔍 Oportunidades',
        'themes_title': '📚 Temas en Conversaciones de Bienestar Latina Más Amplias',
        'themes_desc': '*¿Qué temas se están discutiendo en espacios públicos de bienestar Latina?*',
        'support_preferences': '🤝 Preferencias de Apoyo',
        'support_preferences_desc': '*¿Qué tipos de apoyo está pidiendo la comunidad?*',
        'emotion_support_matching': '🔗 Correspondencia Emoción-Apoyo',
        'emotion_support_desc': '*¿Qué emociones se emparejan con qué solicitudes de apoyo?*',
        'recent_voices': '📝 Voces Comunitarias Recientes',
        'recent_voices_desc': '*Extractos anónimos de historias para entender las necesidades comunitarias*',
        'external_conversations': '🌐 Conversaciones Externas de Muestra',
        'external_conversations_desc': '*Discusiones recientes de blogs, foros y comunidades de bienestar Latina*',
        
        # Página de sanadoras
        'healers_title': '🌺 Nuestro Círculo de Sanadoras',
        'healers_subtitle': 'Conoce a las practicantes de bienestar Latinas sosteniendo espacio para nuestra comunidad',
        'healers_intro': '''Estas practicantes combinan la sabiduría de nuestras ancestras con enfoques terapéuticos modernos.
Honran el *curanderismo*, círculos de oración, remedios herbales y rituales somáticos mientras 
integran coaching informado en trauma, atención plena y psicoeducación.

**Esta plataforma es su herramienta de escucha** - ayudándoles a entender lo que necesitas para 
poder crear ofertas que verdaderamente sirvan a nuestra comunidad.''',
        'healing_philosophy': 'Nuestra Filosofía de Sanación',
        'ancestral_wisdom': '🌿 Sabiduría Ancestral',
        'modern_approaches': '🧠 Enfoques Modernos',
        'how_this_works': '💡 Cómo Funciona Esto',
        'how_this_works_text': '''**💡 Cómo Funciona Esto:**

Estas practicantes usan perspectivas de historias comunitarias anónimas (no detalles individuales) 
para entender qué apoyo se necesita más. Basadas en estos patrones, crean:

- Círculos de sanación grupales
- Talleres y clases  
- Sesiones individuales
- Recursos de autoestudio
- Eventos comunitarios

**Tu voz moldea lo que ofrecemos.** Cuando compartes tu historia, nos ayudas a crear 
exactamente los tipos de apoyo que nuestra comunidad está pidiendo.''',
        'ready_share_story': '🕊️ ¿Lista para Compartir Tu Historia?',
        
        # Panel de Perspectivas - Traducciones adicionales
        'export_data': '📥 Exportar Datos e Informes',
        'export_desc': '*Descarga perspectivas e informes para tus registros*',
        'stories_csv': '📊 Historias CSV',
        'emotions_csv': '😊 Emociones CSV',
        'support_csv': '🤝 Apoyo CSV',
        'external_csv': '🌐 Externo CSV',
        'comprehensive_report': '📄 Informe Completo',
        'report_desc': '📝 Genera un informe de texto completo con todas las perspectivas clave, comparaciones y estadísticas',
        'download_report': '📄 Descargar Informe',
        'key_emotion_insights': '📊 Perspectivas Clave de Emociones',
        'stories': 'historias',
        'of_total': 'del total',
        'more_prominent': '**Más prominente en nuestra comunidad:**',
        'higher': 'más alto',
        'gaining_traction': '**Temas ganando tracción externamente:**',
        'consider_offerings': 'Considera crear ofertas',
        'theme_insights': '💡 **Perspectivas de Temas:** El tema más discutido en conversaciones más amplias es',
        'align_differ': 'Considera cómo las necesidades de nuestra comunidad se alinean o difieren de estas conversaciones más amplias.',
        'show_stories_from': 'Mostrar historias de:',
        'last_7_days': 'Últimos 7 días',
        'last_30_days': 'Últimos 30 días',
        'all_time': 'Todo el tiempo',
        'total_stories_period': 'historias totales en este período',
        'full_story': '**Historia Completa:**',
        'additional_context': '**Contexto Adicional:**',
        'details': '**Detalles:**',
        'date': '**Fecha:**',
        'detected_emotion_label': '**Emoción:**',
        'confidence': 'Confianza:',
        'support_requested': '**Apoyo Solicitado:**',
        'theme': 'Tema:',
        'analysis': '**Análisis:**',
        'page': 'Página',
        'of': 'de',
        'first': '⏮️ Primero',
        'previous': '⬅️ Anterior',
        'next': 'Siguiente ➡️',
        'last': 'Último ⏭️',
        'key_patterns': '💡 Patrones Clave',
        'common_themes': 'Temas Comunes Mencionados',
        'mentioned_times': 'mencionado {count} veces',
        'support_gaps': 'Brechas de Apoyo a Considerar',
        'analyze_themes': '🔍 Analiza si los temas de alta frecuencia tienen opciones de apoyo correspondientes.',
        'consider_offerings_repeated': '💡 Considera crear ofertas que aborden específicamente las preocupaciones repetidas.',
        'suggested_actions': '🎯 Acciones Sugeridas',
        'high_demand': '**Alta Demanda**:',
        'is_most_requested': 'es lo más solicitado',
        'times': 'veces',
        'consider_expanding': 'Considera expandir las ofertas en esta área.',
        'low_awareness': '**Baja Conciencia**: Algunos tipos de apoyo rara vez se seleccionan. Considera educar a la comunidad sobre estas opciones.',
        'active_community': '**Comunidad Activa**:',
        'stories_this_week': 'historias esta semana muestra un fuerte compromiso. ¡Buen momento para lanzar nuevas ofertas!',
        'promote_platform': 'Comienza promoviendo la plataforma a tu comunidad. Comparte el enlace para fomentar la presentación de historias.',
        'footer_privacy': '💚 Este panel respeta el anonimato completo - nunca se almacenan identificadores personales<br>Los datos aquí mostrados representan necesidades comunitarias agregadas, no detalles individuales',
        'logout': '🔓 Cerrar Sesión',
        
        # Más traducciones de Perspectivas
        'emotion_distribution_title': 'Distribución de Emociones en Historias Comunitarias',
        'num_stories_axis': 'Número de Historias',
        'comparison_title': 'Comparación de Emociones: Nuestra Comunidad vs Conversaciones Latinas de Bienestar Más Amplias',
        'percentage_axis': 'Porcentaje (%)',
        'our_community': 'Nuestra Comunidad',
        'broader_discussions': 'Discusiones Más Amplias',
        'theme_distribution_title': 'Distribución de Temas en Contenido Externo',
        'requested_support_types': 'Tipos de Apoyo Solicitados',
        'count': 'Cantidad',
        'emotion_support_heatmap': 'Mapa de Calor de Correlación Emoción-Apoyo',
        'support_type': 'Tipo de Apoyo',
        'emotion': 'Emoción',
        'heatmap_help': '💡 **Cómo leer esto:** Los números muestran cuántas veces cada emoción se emparejó con cada tipo de apoyo. Números más altos (azul más oscuro) indican conexiones más fuertes.',
        'need_stories_comparison': 'Se necesitan tanto historias comunitarias como datos externos para la comparación.',
        'need_stories_heatmap': 'Se necesitan al menos 3 historias para mostrar patrones de emoción-apoyo.',
        'need_emotion_tags': 'Se necesitan más historias con etiquetas de emociones para generar análisis de correlación.',
        'no_stories_period': 'No se encontraron historias para este período de tiempo.',
        'view_breakdown': '📋 Ver Desglose Detallado',
        'blog': 'blog',
        'forum': 'foro',
        'reddit': 'reddit',
        
        # Análisis de Tendencias
        'trend_analysis': '📈 Tendencias de Emociones en el Tiempo',
        'trend_analysis_desc': '*Rastrea cómo evolucionan las emociones comunitarias semana a semana*',
        'select_emotions': 'Selecciona emociones para rastrear:',
        'all_emotions': 'Todas las Emociones',
        'week': 'Semana',
        'emotion_trends_title': 'Tendencias de Emociones Comunitarias',
        'need_data_trends': 'Se necesitan al menos 2 semanas de datos para mostrar tendencias.',
        
        # Filtros Avanzados
        'advanced_filters': '🔍 Filtros Avanzados',
        'filter_by_emotion': 'Filtrar por Emoción:',
        'filter_by_support': 'Filtrar por Tipo de Apoyo:',
        'filter_by_date': 'Filtrar por Rango de Fechas:',
        'all': 'Todas',
        'apply_filters': 'Aplicar Filtros',
        'clear_filters': 'Limpiar Filtros',
        'filtered_results': 'Resultados Filtrados:',
        'matching_stories': 'historias coincidentes',
        
        # Sección de contacto
        'contact_us': 'Contáctanos',
        'get_in_touch': 'Ponte en Contacto',
        'get_in_touch_text': 'Estamos aquí para apoyarte y responder cualquier pregunta.',
        'email': 'Correo:',
        'phone': 'Teléfono:',
        'hours': 'Horario:',
        'need_support': '¿Necesitas Apoyo?',
        'need_support_list': '''- Preguntas sobre la plataforma
- Asistencia técnica
- Consultas de practicantes
- Oportunidades de colaboración
- Recursos generales de bienestar

*Generalmente respondemos en 24 horas.*''',
        'community_guidelines': 'Pautas de la Comunidad',
        'be_respectful': 'Sé Respetuosa',
        'be_respectful_text': 'Honra el viaje y la experiencia de cada persona con compasión.',
        'stay_anonymous': 'Mantén el Anonimato',
        'stay_anonymous_text': 'Protege tu privacidad y la de los demás.',
        'seek_support': 'Busca Apoyo',
        'seek_support_text': 'Esta plataforma te conecta con recursos de sanación.',
    }
}


def get_text(key, lang='en', **kwargs):
    """
    Get translated text for a given key
    Supports string formatting with kwargs
    """
    text = TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text


def get_language_toggle():
    """
    Returns current language setting from session state
    """
    import streamlit as st
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    return st.session_state.language


def set_language(lang):
    """
    Set language in session state
    """
    import streamlit as st
    st.session_state.language = lang
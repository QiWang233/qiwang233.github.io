{% if site.visitor_map.enabled %}
## Visitors

<div class="visitor-map" aria-label="Visitor map">
  {% assign mapmyvisitors_id = site.visitor_map.mapmyvisitors_id | default: "" %}
  {% if mapmyvisitors_id != "" %}
    <script id="mapmyvisitors" type="text/javascript" src="https://mapmyvisitors.com/map.js?d={{ mapmyvisitors_id }}&cl=ffffff&w=a"></script>
  {% else %}
    <div class="visitor-map-placeholder">
      <span>Visitor map is ready.</span>
      <small>Add your MapMyVisitors widget id in <code>_config.yml</code> to enable the live map.</small>
    </div>
  {% endif %}
</div>
{% endif %}

{% if site.visitor_map.enabled %}
## Visitors

<div class="visitor-map" aria-label="Visitor map">
  {% assign clustrmaps_id = site.visitor_map.clustrmaps_id | default: "" %}
  {% if clustrmaps_id != "" %}
    <script id="clustrmaps" type="text/javascript" src="https://cdn.clustrmaps.com/map_v2.js?cl=0f172a&w=300&t=tt&d={{ clustrmaps_id }}&co=ffffff&cmn=93c5fd&cmo=2563eb&ct=0f172a"></script>
  {% else %}
    <div class="visitor-map-placeholder">
      <span>Visitor map is ready.</span>
      <small>Add your ClustrMaps widget id in <code>_config.yml</code> to enable the live map.</small>
    </div>
  {% endif %}
</div>
{% endif %}
